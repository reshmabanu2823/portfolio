import os
import shutil
import re
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded"

src_img = os.path.join(UPLOAD_DIR, "media_1788157395547.jpg")
im = Image.open(src_img)
print(f"Source ascenseur image: size={im.size}, mode={im.mode}")

assets_dir = os.path.join(WORKSPACE, "assets")
www_assets_dir = os.path.join(WORKSPACE, "www.noth.in", "assets")
os.makedirs(assets_dir, exist_ok=True)
os.makedirs(www_assets_dir, exist_ok=True)

# Save WebP and original JPG
bg_webp_name = "ascenseur_bg.webp"
bg_jpg_name = "ascenseur_bg.jpg"

im.save(os.path.join(assets_dir, bg_webp_name), "WEBP", quality=96)
im.save(os.path.join(www_assets_dir, bg_webp_name), "WEBP", quality=96)
shutil.copyfile(src_img, os.path.join(assets_dir, bg_jpg_name))
shutil.copyfile(src_img, os.path.join(www_assets_dir, bg_jpg_name))

# Generate responsive variants
orig_w, orig_h = im.size
aspect = orig_h / orig_w
for width in [500, 800, 1080, 1600, 1920]:
    target_w = min(width, orig_w)
    target_h = int(target_w * aspect)
    resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    fname = f"ascenseur_bg-p-{width}.webp" if width < 1920 else bg_webp_name
    resized.save(os.path.join(assets_dir, fname), "WEBP", quality=94)
    resized.save(os.path.join(www_assets_dir, fname), "WEBP", quality=94)
    print(f"Generated {fname} ({target_w}x{target_h})")

# Update HTML files
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_img_pattern = r'<img[^>]*class="img-ascenseur"[^>]*>'
new_img_tag = '<img src="/assets/ascenseur_bg.webp" loading="eager" sizes="100vw" srcset="/assets/ascenseur_bg-p-500.webp 500w, /assets/ascenseur_bg-p-800.webp 800w, /assets/ascenseur_bg-p-1080.webp 1080w, /assets/ascenseur_bg-p-1600.webp 1600w, /assets/ascenseur_bg.webp 1920w" alt="Dark Textured Elevator Studio Background" class="img-ascenseur"/>'

matches = re.findall(old_img_pattern, html)
print(f"Found {len(matches)} matches for img-ascenseur")

html = re.sub(old_img_pattern, new_img_tag, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced img-ascenseur with new attached image!")
