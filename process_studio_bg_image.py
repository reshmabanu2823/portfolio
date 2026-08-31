import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded"

src_img = os.path.join(UPLOAD_DIR, "media_1788159996636.png")
im = Image.open(src_img)
print(f"Source 3D studio image: size={im.size}, mode={im.mode}")

# Create background folders
bg_dir = os.path.join(WORKSPACE, "assets", "backgrounds")
www_bg_dir = os.path.join(WORKSPACE, "www.noth.in", "assets", "backgrounds")
os.makedirs(bg_dir, exist_ok=True)
os.makedirs(www_bg_dir, exist_ok=True)

# Save as studio-bg-light.jpg and studio-bg-light.webp (full quality)
jpg_name = "studio-bg-light.jpg"
webp_name = "studio-bg-light.webp"

# Convert RGBA to RGB for JPEG if necessary
rgb_im = im.convert("RGB") if im.mode in ("RGBA", "P") else im

rgb_im.save(os.path.join(bg_dir, jpg_name), "JPEG", quality=95)
rgb_im.save(os.path.join(www_bg_dir, jpg_name), "JPEG", quality=95)

im.save(os.path.join(bg_dir, webp_name), "WEBP", quality=95)
im.save(os.path.join(www_bg_dir, webp_name), "WEBP", quality=95)

print(f"Successfully saved {jpg_name} and {webp_name} to assets/backgrounds/")
