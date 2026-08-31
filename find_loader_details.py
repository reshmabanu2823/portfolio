import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find loader markup
loader_match = re.search(r'(<div class="loader-img-w">)(.*?)(</div>)', html, flags=re.DOTALL)
if loader_match:
    print("Found loader images:")
    imgs = re.findall(r'<img[^>]+>', loader_match.group(2))
    for i, img in enumerate(imgs):
        print(f"  {i}: {img}")

# Find any JS referencing loader-img
scripts = re.findall(r'(\.loader-img[^\n;]+)', html)
print(f"Found {len(scripts)} references to loader-img:")
for s in scripts[:10]:
    print(f"  {s}")
