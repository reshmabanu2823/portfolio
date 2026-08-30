"""
=============================================================================
  CINEMATIC 3D TYPOGRAPHY ANIMATION RENDERER: "RESHMA BANU" (ROI ACCELERATED)
=============================================================================
High-performance procedural renderer producing a 35-second 1080p seamless
looping video with 10 continuous material morphing states.
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

OUTPUT_MP4 = os.path.join(WORKSPACE, 'reshma_banu_3d_typography.mp4')
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WIDTH = 1920
HEIGHT = 1080
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

# Active typography ROI
ROI_Y1, ROI_Y2 = 180, 900
ROI_X1, ROI_X2 = 120, 1800
ROI_H = ROI_Y2 - ROI_Y1
ROI_W = ROI_X2 - ROI_X1

def load_and_preprocess_states():
    print("Loading and normalizing 10 material target states...")
    processed_roi = []
    target_w = int(WIDTH * 0.78)  # ~1497px width

    for name, fname in STATE_FILES:
        p = os.path.join(UPLOAD_DIR, fname)
        im = Image.open(p).convert('RGBA')
        np_im = np.array(im)

        rgb = np_im[:, :, :3]
        alpha = np_im[:, :, 3] if np_im.shape[2] == 4 else np.ones(rgb.shape[:2], dtype=np.uint8)*255
        
        mask = (rgb.sum(axis=2) > 15) | (alpha > 30)
        y_indices, x_indices = np.where(mask)
        
        if len(y_indices) > 0 and len(x_indices) > 0:
            ymin, ymax = y_indices.min(), y_indices.max()
            xmin, xmax = x_indices.min(), x_indices.max()
            cropped = im.crop((xmin, ymin, xmax, ymax))
        else:
            cropped = im

        crop_w, crop_h = cropped.size
        scale = target_w / float(crop_w)
        new_w = target_w
        new_h = int(crop_h * scale)
        resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)

        canvas = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
        paste_x = (WIDTH - new_w) // 2
        paste_y = (HEIGHT - new_h) // 2
        canvas.paste(resized, (paste_x, paste_y), resized if resized.mode == 'RGBA' else None)

        full_arr = np.array(canvas, dtype=np.uint8)
        roi_arr = full_arr[ROI_Y1:ROI_Y2, ROI_X1:ROI_X2].copy()
        processed_roi.append(roi_arr)
        print(f"  Loaded state ROI: {name} -> {ROI_W}x{ROI_H}")

    return processed_roi

def compute_optical_flow_roi(img_a, img_b):
    g_a = cv2.cvtColor(img_a, cv2.COLOR_RGB2GRAY)
    g_b = cv2.cvtColor(img_b, cv2.COLOR_RGB2GRAY)

    scale = 0.35
    small_a = cv2.resize(g_a, (0,0), fx=scale, fy=scale)
    small_b = cv2.resize(g_b, (0,0), fx=scale, fy=scale)

    flow_forward = cv2.calcOpticalFlowFarneback(
        small_a, small_b, None,
        pyr_scale=0.5, levels=3, winsize=13,
        iterations=2, poly_n=5, poly_sigma=1.1, flags=0
    )
    flow_backward = cv2.calcOpticalFlowFarneback(
        small_b, small_a, None,
        pyr_scale=0.5, levels=3, winsize=13,
        iterations=2, poly_n=5, poly_sigma=1.1, flags=0
    )

    flow_f = cv2.resize(flow_forward, (ROI_W, ROI_H)) / scale
    flow_b = cv2.resize(flow_backward, (ROI_W, ROI_H)) / scale

    return flow_f.astype(np.float32), flow_b.astype(np.float32)

def smoothstep(x):
    x = max(0.0, min(1.0, float(x)))
    return x * x * (3.0 - 2.0 * x)

def render_animation():
    states_roi = load_and_preprocess_states()

    print("\nPrecomputing physical morph flow fields...")
    flows = []
    for i in range(len(states_roi) - 1):
        f_f, f_b = compute_optical_flow_roi(states_roi[i], states_roi[i+1])
        flows.append((f_f, f_b))
        print(f"  Flow computed: State {i+1} <-> State {i+2}")

    # Pre-allocate ROI grids
    grid_x, grid_y = np.meshgrid(np.arange(ROI_W, dtype=np.float32), np.arange(ROI_H, dtype=np.float32))
    map_x_a = np.empty((ROI_H, ROI_W), dtype=np.float32)
    map_y_a = np.empty((ROI_H, ROI_W), dtype=np.float32)
    map_x_b = np.empty((ROI_H, ROI_W), dtype=np.float32)
    map_y_b = np.empty((ROI_H, ROI_W), dtype=np.float32)

    # Lighting sweep coordinate grid in ROI
    x_coords = np.linspace(-1.0, 1.0, ROI_W, dtype=np.float32)
    y_coords = np.linspace(-0.5, 0.5, ROI_H, dtype=np.float32)
    X, Y = np.meshgrid(x_coords, y_coords)

    # Output full frame buffer
    full_frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    print(f"\nStarting FFmpeg video encoding: {OUTPUT_MP4}")
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
        '-preset', 'ultrafast',
        '-crf', '18',
        '-movflags', '+faststart',
        OUTPUT_MP4
    ]

    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    print("Rendering 1050 frames (35.0s @ 30fps)...")

    frame_count = 0
    for seg_idx, (f_start, f_end, s_from, s_to, mode) in enumerate(SEGMENTS):
        seg_frames = f_end - f_start
        print(f"  Rendering Segment {seg_idx+1}/10: Frames {f_start}..{f_end} ({mode})")

        img_a = states_roi[s_from]
        img_b = states_roi[s_to]
        if mode == "morph":
            flow_f, flow_b = flows[s_from]

        for f in range(f_start, f_end):
            local_t = (f - f_start) / float(seg_frames)

            # 1. Subtle Organic Breathing & Floating
            float_y = math.sin(f * 2 * math.pi / 150.0) * 3.5
            float_x = math.cos(f * 2 * math.pi / 350.0) * 1.5

            if mode == "intro_glass":
                fade = smoothstep(local_t / 0.65)
                f_float = (img_a.astype(np.float32) * fade)

                # Caustic glimmer
                shimmer_x = -1.2 + local_t * 2.4
                glint = (np.exp(-((X - shimmer_x) ** 2) / 0.06) * np.exp(-(Y ** 2) / 0.12)).astype(np.float32)
                mask = (f_float.sum(axis=2) > 10).astype(np.float32)
                for c in range(3):
                    f_float[:, :, c] += glint * mask * 90.0 * (1.0 - local_t)

                roi_uint8 = np.clip(f_float, 0, 255).astype(np.uint8)

            else:
                t_ease = smoothstep(local_t)

                np.add(grid_x, flow_f[:, :, 0] * t_ease, out=map_x_a)
                np.add(grid_y, flow_f[:, :, 1] * t_ease, out=map_y_a)

                weight_b = 1.0 - t_ease
                np.add(grid_x, flow_b[:, :, 0] * weight_b, out=map_x_b)
                np.add(grid_y, flow_b[:, :, 1] * weight_b, out=map_y_b)

                warped_a = cv2.remap(img_a, map_x_a, map_y_a, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
                warped_b = cv2.remap(img_b, map_x_b, map_y_b, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

                blended = cv2.addWeighted(warped_a, 1.0 - t_ease, warped_b, t_ease, 0.0)

                # Dynamic light sheen sweep
                sweep_x = -1.4 + t_ease * 2.8
                sheen = (np.exp(-((X - sweep_x) ** 2) / 0.05) * math.sin(t_ease * math.pi) * 50.0).astype(np.float32)
                mask = (blended.sum(axis=2) > 10).astype(np.float32)

                if s_from in (2, 3, 4):
                    sheen_r, sheen_g, sheen_b = 1.0, 0.85, 1.0
                elif s_from in (5, 6):
                    sheen_r, sheen_g, sheen_b = 0.95, 0.95, 1.0
                elif s_from == 8:
                    sheen_r, sheen_g, sheen_b = 1.0, 0.7, 0.85
                else:
                    sheen_r, sheen_g, sheen_b = 0.9, 0.95, 1.0

                blended_f = blended.astype(np.float32)
                blended_f[:, :, 0] += sheen * mask * sheen_r
                blended_f[:, :, 1] += sheen * mask * sheen_g
                blended_f[:, :, 2] += sheen * mask * sheen_b

                roi_uint8 = np.clip(blended_f, 0, 255).astype(np.uint8)

            # Apply Floating / Breathing to ROI
            if abs(float_y) > 0.05 or abs(float_x) > 0.05:
                M = np.float32([[1.0, 0, float_x],
                                [0, 1.0, float_y]])
                roi_uint8 = cv2.warpAffine(roi_uint8, M, (ROI_W, ROI_H), borderMode=cv2.BORDER_CONSTANT, borderValue=0)

            # Insert ROI into 1920x1080 full frame
            full_frame[ROI_Y1:ROI_Y2, ROI_X1:ROI_X2] = roi_uint8
            pipe.stdin.write(full_frame.tobytes())
            frame_count += 1

    pipe.stdin.close()
    pipe.wait()

    print("=" * 60)
    print("  RENDER COMPLETE!")
    print(f"  Total Frames Rendered: {frame_count}")
    print(f"  Output MP4: {OUTPUT_MP4}")
    print(f"  File Size : {os.path.getsize(OUTPUT_MP4) / (1024*1024):.2f} MB")
    print("=" * 60)

if __name__ == '__main__':
    render_animation()
