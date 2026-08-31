import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Search for the 4 images in the studio section or across HTML
img_tags = re.findall(r'<img[^>]+>', html)
print(f"Total img tags: {len(img_tags)}")
for img in img_tags:
    if 'cert' in img.lower() or 'google' in img.lower() or 'intel' in img.lower() or 'simplilearn' in img.lower() or 'appreciat' in img.lower() or 'studio' in img.lower():
        print("  ", img)
