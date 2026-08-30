import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="formes-w"')
end_idx = c.find('</section>', idx)
section = c[idx:end_idx]

svgs = re.findall(r'<svg[^>]*class="[^"]*-cursor[^"]*"[^>]*>.*?</svg>', section, flags=re.DOTALL)
print(f'Found {len(svgs)} cursor SVGs:')
for s in svgs:
    class_name = re.search(r'class="([^"]*)"', s).group(1)
    viewBox = re.search(r'viewBox="([^"]*)"', s).group(1) if 'viewBox' in s else 'None'
    print(f'Class: {class_name}, viewBox: {viewBox}, len: {len(s)}')
