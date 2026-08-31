import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

# 1. Process image
img_src = os.path.join(UPLOAD_DIR, 'media_1788150073229.png')
im = Image.open(img_src)
print("Uploaded Lumina image size:", im.size)

proj_dir = os.path.join(WORKSPACE, 'assets', 'projects')
www_proj_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'projects')
os.makedirs(proj_dir, exist_ok=True)
os.makedirs(www_proj_dir, exist_ok=True)

im.save(os.path.join(proj_dir, 'lumina.webp'), 'WEBP', quality=95)
im.save(os.path.join(www_proj_dir, 'lumina.webp'), 'WEBP', quality=95)
shutil.copyfile(img_src, os.path.join(proj_dir, 'lumina.png'))
shutil.copyfile(img_src, os.path.join(www_proj_dir, 'lumina.png'))
print("Saved Lumina project image assets!")

# 2. Update HTML
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Replace the utopia work vignette image
old_src = r'https://cdn\.prod\.website-files\.com/6a2679b9acc91890e34df140/6a319bb9740ace5d22b1065c_work-vignette-utopia-V2\.webp'
old_img_tag = r'<img src="https://cdn\.prod\.website-files\.com/6a2679b9acc91890e34df140/6a319bb9740ace5d22b1065c_work-vignette-utopia-V2\.webp"[^>]*class="img-work"[^>]*>'

# Find matching tags
matches = re.findall(old_img_tag, html)
print(f"Found {len(matches)} matching img-work tags for utopia")

new_img_tag = '<img src="/assets/projects/lumina.webp" loading="eager" alt="Lumina - Reshma Banu" sizes="100vw" srcset="/assets/projects/lumina.webp 1600w" class="img-work"/>'

html = re.sub(old_img_tag, new_img_tag, html)
html = html.replace('https://cdn.prod.website-files.com/6a2679b9acc91890e34df140/6a319bb9740ace5d22b1065c_work-vignette-utopia-V2.webp', '/assets/projects/lumina.webp')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML with Lumina project image!")
