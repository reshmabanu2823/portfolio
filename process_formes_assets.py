import os
import shutil
from PIL import Image, ImageOps

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

def process_forme(src_path, name):
    im = Image.open(src_path).convert("RGBA")
    
    # Check if we can create a clean alpha mask where pure black (R+G+B < 8) is smoothly transparent
    # For black_puzzle (which has shiny black subject on black bg), use threshold or keep RGB
    # Since background is pure black, saving high quality webp with RGB/RGBA:
    out_orig = os.path.join(formes_dir, f"{name}.webp")
    im.save(out_orig, "WEBP", quality=95)
    shutil.copy(out_orig, os.path.join(formes_dir_www, f"{name}.webp"))
    
    # Also create responsive variants: 500w, 800w, 1080w
    for width in [500, 800, 1080]:
        h = int(im.height * (width / im.width))
        resized = im.resize((width, h), Image.Resampling.LANCZOS)
        out_v = os.path.join(formes_dir, f"{name}-p-{width}.webp")
        resized.save(out_v, "WEBP", quality=90)
        shutil.copy(out_v, os.path.join(formes_dir_www, f"{name}-p-{width}.webp"))
    
    print(f"Processed {name} into webp and responsive variants!")

for k, path in uploaded.items():
    process_forme(path, k)

print("All 3D shape assets successfully created in /assets/formes/!")
