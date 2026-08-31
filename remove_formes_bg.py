import os
import shutil
import numpy as np
from PIL import Image, ImageFilter

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
formes_dir = os.path.join(WORKSPACE, 'assets', 'formes')
formes_dir_www = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'formes')
os.makedirs(formes_dir, exist_ok=True)
os.makedirs(formes_dir_www, exist_ok=True)

uploaded = {
    'blue_knot': r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189156916.jpg",
    'pink_network': r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189148184.jpg",
    'disco_ball': r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189115452.jpg",
    'black_puzzle': r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189099354.png",
    'bubble_gear': r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189107329.jpg",
}

def remove_black_background(img_path, name):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    rgb = arr[:, :, :3]
    
    # Calculate max channel and luminance
    max_c = np.max(rgb, axis=2)
    luminance = 0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]
    
    if name == 'black_puzzle':
        # Black puzzle has dark shiny body on black background
        # Use threshold with gentle ramp: pixels with any reflection or specular highlights
        # Since background is pure black (0-3), threshold at 6 with smooth ramp up to 24
        alpha = np.clip((max_c - 4.0) / 18.0 * 255.0, 0, 255)
        # For the dark body inside the puzzle outline, we know it's a solid shape
        # Let's perform a morphological fill / flood from center or convex threshold
        from scipy.ndimage import binary_fill_holes
        mask_binary = max_c > 5.0
        filled = binary_fill_holes(mask_binary)
        alpha = np.where(filled, np.maximum(alpha, 255.0), 0.0)
    elif name == 'bubble_gear':
        # Glass bubble gear on black background -> screen/luminance based transparency
        alpha = np.clip((luminance - 2.0) / 25.0 * 255.0, 0, 255)
    elif name in ['blue_knot', 'pink_network']:
        # Colorful 3D renders on black -> clean alpha mask based on max color / luminance
        alpha = np.clip((max_c - 3.0) / 15.0 * 255.0, 0, 255)
    elif name == 'disco_ball':
        # Disco ball is a perfect sphere in the center with reflections
        # Create circular alpha mask with edge antialiasing
        h, w = im.size
        cy, cx = h / 2.0, w / 2.0
        y, x = np.ogrid[:h, :w]
        dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        # Find sphere radius where reflections exist (~0.355 * w)
        radius = w * 0.355
        circle_mask = np.clip((radius + 1.5 - dist) / 2.0 * 255.0, 0, 255)
        alpha = np.minimum(circle_mask, np.clip((max_c - 2.0) / 10.0 * 255.0, 0, 255))
        alpha = np.where(dist <= radius - 2, 255.0, alpha)
    else:
        alpha = np.clip((max_c - 4.0) / 16.0 * 255.0, 0, 255)

    arr[:, :, 3] = alpha
    out_im = Image.fromarray(arr.astype(np.uint8), "RGBA")
    
    # Save transparent PNG and WebP
    png_path = os.path.join(formes_dir, f"{name}.png")
    webp_path = os.path.join(formes_dir, f"{name}.webp")
    out_im.save(png_path, "PNG")
    out_im.save(webp_path, "WEBP", quality=95)
    
    shutil.copy(png_path, os.path.join(formes_dir_www, f"{name}.png"))
    shutil.copy(webp_path, os.path.join(formes_dir_www, f"{name}.webp"))
    
    # Responsive variants
    for width in [500, 800, 1080]:
        h = int(out_im.height * (width / out_im.width))
        resized = out_im.resize((width, h), Image.Resampling.LANCZOS)
        out_v = os.path.join(formes_dir, f"{name}-p-{width}.webp")
        resized.save(out_v, "WEBP", quality=92)
        shutil.copy(out_v, os.path.join(formes_dir_www, f"{name}-p-{width}.webp"))
        
    print(f"Background successfully removed and saved for {name}!")

for k, path in uploaded.items():
    try:
        remove_black_background(path, k)
    except Exception as e:
        print(f"Error processing {k}: {e}")
        # Fallback if scipy not present
        im = Image.open(path).convert("RGBA")
        arr = np.array(im, dtype=np.float32)
        max_c = np.max(arr[:, :, :3], axis=2)
        alpha = np.clip((max_c - 4.0) / 16.0 * 255.0, 0, 255)
        arr[:, :, 3] = alpha
        out_im = Image.fromarray(arr.astype(np.uint8), "RGBA")
        out_orig = os.path.join(formes_dir, f"{k}.webp")
        out_im.save(out_orig, "WEBP", quality=95)
        shutil.copy(out_orig, os.path.join(formes_dir_www, f"{k}.webp"))
        print(f"Processed {k} with fallback alpha matting!")
