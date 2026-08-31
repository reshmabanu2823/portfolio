import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

src_p = os.path.join(UPLOAD_DIR, 'media_1788150529796.png')
im = Image.open(src_p)
print(f"Original image size: {im.size}, mode: {im.mode}")

# Directories
work_dir = os.path.join(WORKSPACE, 'assets', 'work')
www_work_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work')
os.makedirs(work_dir, exist_ok=True)
os.makedirs(www_work_dir, exist_ok=True)

# 1. Full original PNG and WebP
shutil.copyfile(src_p, os.path.join(work_dir, 'musicify-screenshot.png'))
shutil.copyfile(src_p, os.path.join(www_work_dir, 'musicify-screenshot.png'))

im_rgb = im.convert('RGB') if im.mode in ('RGBA', 'LA') else im
im.save(os.path.join(work_dir, 'musicify-screenshot.webp'), 'WEBP', quality=95, lossless=False)
im.save(os.path.join(www_work_dir, 'musicify-screenshot.webp'), 'WEBP', quality=95, lossless=False)

# 2. Generate responsive variants (500w, 800w, 1080w, 1600w)
orig_w, orig_h = im.size
aspect = orig_h / orig_w

for width in [500, 800, 1080, 1600]:
    target_w = min(width, orig_w)
    target_h = int(target_w * aspect)
    resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    fname = f'musicify-screenshot-p-{width}.webp' if width < 1600 else 'musicify-screenshot.webp'
    resized.save(os.path.join(work_dir, fname), 'WEBP', quality=92)
    resized.save(os.path.join(www_work_dir, fname), 'WEBP', quality=92)
    print(f"Generated {fname} ({target_w}x{target_h})")

# 3. Update HTML
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Find the work-vignette / lumina img tag
old_pattern = r'<img\s+src="[^"]*(?:work-vignette-utopia|lumina)[^"]*"\s+[^>]*class="img-work"[^>]*>'

new_tag = '<img src="/assets/work/musicify-screenshot.webp" loading="eager" alt="Musicify — music streaming app dashboard" sizes="100vw" srcset="/assets/work/musicify-screenshot-p-500.webp 500w, /assets/work/musicify-screenshot-p-800.webp 800w, /assets/work/musicify-screenshot-p-1080.webp 1080w, /assets/work/musicify-screenshot.webp 1600w" class="img-work" style="top: 0px; object-fit: cover; width: 100%; height: auto; translate: none; rotate: none; scale: none; transform: translate(0%, -16.8824%) translate3d(0px, 0px, 0px);"/>'

matches = re.findall(old_pattern, html)
print(f"Found {len(matches)} matches to replace")
html = re.sub(old_pattern, new_tag, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced project vignette image with Musicify assets and responsive srcset!")
