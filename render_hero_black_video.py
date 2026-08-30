"""
=============================================================================
  HERO 3D TYPOGRAPHY RENDERER: BLACK STUDIO BACKGROUND
=============================================================================
Renders the 35-second seamless looping video with:
- Pure Black Studio Background (#000000 / rgb(0,0,0))
- 10-state continuous physical material morphing
- Aspect ratio: 1920 x 210 (matching viewBox 0 0 2679.8 294)
- Web-optimized H.264 MP4 with +faststart
=============================================================================
"""

import os
import sys
import math
import subprocess
import numpy as np
from PIL import Image
import cv2
import imageio_ffmpeg

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

OUTPUT_MP4 = os.path.join(WORKSPACE, 'reshma_banu_hero_3d.mp4')
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WIDTH = 1920
HEIGHT = 210
FPS = 30
TOTAL_SECONDS = 35
TOTAL_FRAMES = FPS * TOTAL_SECONDS  # 1050 frames

STATE_FILES = [
    ('1_glass', 'media_1788082296074.png'),
    ('2_chrome', 'media_1788083769491.png'),
    ('3_black_foil', 'media_1788082309155.png'),
    ('4_blue_purple', 'media_1788082299712.png'),
    ('5_hot_pink', 'media_1788082302699.png'),
    ('6_white_fluff', 'media_1788083811552.png'),
    ('7_white_fabric', 'media_1788083717282.png'),
    ('8_white_foam', 'media_1788082312015.png'),
    ('9_pink_icing', 'media_1788083777457.png'),
    ('10_glass_loop', 'media_1788082296074.png')
]

SEGMENTS = [
    (0, 120, 0, 0, "intro_glass"),
    (120, 240, 0, 1, "morph"),
    (240, 360, 1, 2, "morph"),
    (360, 480, 2, 3, "morph"),
    (480, 600, 3, 4, "morph"),
    (600, 720, 4, 5, "morph"),
    (720, 810, 5, 6, "morph"),
    (810, 900, 6, 7, "morph"),
    (900, 990, 7, 8, "morph"),
    (990, 1050, 8, 9, "morph")
]

def load_and_preprocess_states():
    print("Loading and normalizing 10 material target states for black studio background...")
    processed_rgb = []
    processed_alpha = []
    target_w = int(WIDTH * 0.98)

    for name, fname in STATE_FILES:
        p = os.path.join(UPLOAD_DIR, fname)
        im = Image.open(p).convert('RGBA')
        np_im = np.array(im, dtype=np.float32) / 255.0
        rgb = np_im[:, :, :3]

        max_c = rgb.max(axis=2)
        gray = (max_c * 255).astype(np.uint8)
        _, thresh = cv2.threshold(gray, 6, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(gray, dtype=np.float32)
        cv2.drawContours(mask, contours, -1, 1.0, -1)
        mask = cv2.GaussianBlur(mask, (3, 3), 0.8)

        if 'glass' in name:
            mask = np.maximum(mask, np.clip(max_c * 1.5, 0, 1))

        y_idx, x_idx = np.where(mask > 0.03)
        if len(y_idx) > 0 and len(x_idx) > 0:
            ymin, ymax = y_idx.min(), y_idx.max()
            xmin, xmax = x_idx.min(), x_idx.max()
        else:
            ymin, ymax, xmin, xmax = 0, im.height, 0, im.width

        crop_rgb = rgb[ymin:ymax, xmin:xmax]
        crop_alpha = mask[ymin:ymax, xmin:xmax]

        crop_h, crop_w = crop_rgb.shape[:2]
        scale = target_w / float(crop_w)
        new_w = target_w
        new_h = int(crop_h * scale)

        if new_h > HEIGHT - 10:
            scale = (HEIGHT - 10) / float(crop_h)
            new_h = HEIGHT - 10
            new_w = int(crop_w * scale)

        resized_rgb = cv2.resize(crop_rgb, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
        resized_alpha = cv2.resize(crop_alpha, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)

        canvas_rgb = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
        canvas_alpha = np.zeros((HEIGHT, WIDTH), dtype=np.float32)

        paste_x = (WIDTH - new_w) // 2
        paste_y = (HEIGHT - new_h) // 2

        canvas_rgb[paste_y:paste_y+new_h, paste_x:paste_x+new_w] = resized_rgb
        canvas_alpha[paste_y:paste_y+new_h, paste_x:paste_x+new_w] = resized_alpha

        processed_rgb.append(canvas_rgb)
        processed_alpha.append(canvas_alpha)
        print(f"  Processed {name}: {new_w}x{new_h} in {WIDTH}x{HEIGHT}")

    return processed_rgb, processed_alpha

def compute_optical_flow(img_a, img_b):
    g_a = (img_a.mean(axis=2) * 255).astype(np.uint8)
    g_b = (img_b.mean(axis=2) * 255).astype(np.uint8)

    scale = 0.35
    small_a = cv2.resize(g_a, (0,0), fx=scale, fy=scale)
    small_b = cv2.resize(g_b, (0,0), fx=scale, fy=scale)

    flow_forward = cv2.calcOpticalFlowFarneback(
        small_a, small_b, None,
        pyr_scale=0.5, levels=3, winsize=11,
        iterations=2, poly_n=5, poly_sigma=1.1, flags=0
    )
    flow_backward = cv2.calcOpticalFlowFarneback(
        small_b, small_a, None,
        pyr_scale=0.5, levels=3, winsize=11,
        iterations=2, poly_n=5, poly_sigma=1.1, flags=0
    )

    flow_f = cv2.resize(flow_forward, (WIDTH, HEIGHT)) / scale
    flow_b = cv2.resize(flow_backward, (WIDTH, HEIGHT)) / scale

    return flow_f.astype(np.float32), flow_b.astype(np.float32)

def smoothstep(x):
    x = max(0.0, min(1.0, float(x)))
    return x * x * (3.0 - 2.0 * x)

def render_black_hero_video():
    states_rgb, states_alpha = load_and_preprocess_states()

    print("\nComputing morph optical flows...")
    flows = []
    for i in range(len(states_rgb) - 1):
        f_f, f_b = compute_optical_flow(states_rgb[i], states_rgb[i+1])
        flows.append((f_f, f_b))
        print(f"  Flow: State {i+1} <-> State {i+2}")

    grid_x, grid_y = np.meshgrid(np.arange(WIDTH, dtype=np.float32), np.arange(HEIGHT, dtype=np.float32))
    map_x_a = np.empty((HEIGHT, WIDTH), dtype=np.float32)
    map_y_a = np.empty((HEIGHT, WIDTH), dtype=np.float32)
    map_x_b = np.empty((HEIGHT, WIDTH), dtype=np.float32)
    map_y_b = np.empty((HEIGHT, WIDTH), dtype=np.float32)

    x_coords = np.linspace(-1.0, 1.0, WIDTH, dtype=np.float32)
    y_coords = np.linspace(-0.5, 0.5, HEIGHT, dtype=np.float32)
    X, Y = np.meshgrid(x_coords, y_coords)

    print(f"\nEncoding Black Background Hero Video: {OUTPUT_MP4}")
    ffmpeg_cmd = [
        FFMPEG_EXE, '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{WIDTH}x{HEIGHT}',
        '-pix_fmt', 'rgb24',
        '-r', str(FPS),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-profile:v', 'high',
        '-preset', 'veryfast',
        '-crf', '17',
        '-movflags', '+faststart',
        OUTPUT_MP4
    ]

    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    print(f"Rendering 1050 frames ({WIDTH}x{HEIGHT} on pure black background)...")

    frame_count = 0
    for seg_idx, (f_start, f_end, s_from, s_to, mode) in enumerate(SEGMENTS):
        seg_frames = f_end - f_start
        print(f"  Segment {seg_idx+1}/10: Frames {f_start}..{f_end}")

        rgb_a = states_rgb[s_from]
        alpha_a = states_alpha[s_from]
        rgb_b = states_rgb[s_to]
        alpha_b = states_alpha[s_to]

        if mode == "morph":
            flow_f, flow_b = flows[s_from]

        for f in range(f_start, f_end):
            local_t = (f - f_start) / float(seg_frames)

            # Floating / breathing
            float_y = math.sin(f * 2 * math.pi / 150.0) * 1.8
            float_x = math.cos(f * 2 * math.pi / 350.0) * 0.8

            if mode == "intro_glass":
                fade = smoothstep(local_t / 0.7)
                curr_alpha = alpha_a * fade
                curr_rgb = rgb_a * fade

                shimmer_x = -1.2 + local_t * 2.4
                glint = (np.exp(-((X - shimmer_x) ** 2) / 0.05) * np.exp(-(Y ** 2) / 0.15)).astype(np.float32)
                curr_rgb += glint[:, :, None] * curr_alpha[:, :, None] * 0.45 * (1.0 - local_t)

            else:
                t_ease = smoothstep(local_t)

                np.add(grid_x, flow_f[:, :, 0] * t_ease, out=map_x_a)
                np.add(grid_y, flow_f[:, :, 1] * t_ease, out=map_y_a)

                weight_b = 1.0 - t_ease
                np.add(grid_x, flow_b[:, :, 0] * weight_b, out=map_x_b)
                np.add(grid_y, flow_b[:, :, 1] * weight_b, out=map_y_b)

                warped_rgb_a = cv2.remap(rgb_a, map_x_a, map_y_a, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
                warped_alpha_a = cv2.remap(alpha_a, map_x_a, map_y_a, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

                warped_rgb_b = cv2.remap(rgb_b, map_x_b, map_y_b, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
                warped_alpha_b = cv2.remap(alpha_b, map_x_b, map_y_b, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

                curr_rgb = warped_rgb_a * (1.0 - t_ease) + warped_rgb_b * t_ease
                curr_alpha = warped_alpha_a * (1.0 - t_ease) + warped_alpha_b * t_ease

                # Light sweep
                sweep_x = -1.4 + t_ease * 2.8
                sheen = (np.exp(-((X - sweep_x) ** 2) / 0.04) * math.sin(t_ease * math.pi) * 0.25).astype(np.float32)

                if s_from in (2, 3, 4):
                    sheen_color = np.array([1.0, 0.85, 1.0], dtype=np.float32)
                elif s_from in (5, 6):
                    sheen_color = np.array([0.95, 0.95, 1.0], dtype=np.float32)
                elif s_from == 8:
                    sheen_color = np.array([1.0, 0.7, 0.85], dtype=np.float32)
                else:
                    sheen_color = np.array([0.9, 0.95, 1.0], dtype=np.float32)

                curr_rgb += sheen[:, :, None] * curr_alpha[:, :, None] * sheen_color[None, None, :]

            # Subtle floating offset
            if abs(float_y) > 0.05 or abs(float_x) > 0.05:
                M = np.float32([[1.0, 0, float_x],
                                [0, 1.0, float_y]])
                curr_rgb = cv2.warpAffine(curr_rgb, M, (WIDTH, HEIGHT), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
                curr_alpha = cv2.warpAffine(curr_alpha, M, (WIDTH, HEIGHT), borderMode=cv2.BORDER_CONSTANT, borderValue=0)

            # COMPOSITE ONTO PURE BLACK BACKGROUND (#000000 / rgb(0,0,0))
            curr_alpha = np.clip(curr_alpha, 0.0, 1.0)[:, :, None]
            curr_rgb = np.clip(curr_rgb, 0.0, 1.0)
            composited = curr_rgb * curr_alpha  # Background is (0, 0, 0)

            frame_uint8 = (np.clip(composited, 0.0, 1.0) * 255.0).astype(np.uint8)
            pipe.stdin.write(frame_uint8.tobytes())
            frame_count += 1

    pipe.stdin.close()
    pipe.wait()

    print("=" * 60)
    print("  BLACK HERO RENDER COMPLETE!")
    print(f"  Frames Rendered: {frame_count}")
    print(f"  Output MP4    : {OUTPUT_MP4}")
    print(f"  File Size     : {os.path.getsize(OUTPUT_MP4) / (1024*1024):.2f} MB")
    print("=" * 60)

if __name__ == '__main__':
    render_black_hero_video()
