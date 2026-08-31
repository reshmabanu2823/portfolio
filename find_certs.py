import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

matches = [m.start() for m in re.finditer(r'Google Cloud|Certificate|img-studio|studio-grid', html, flags=re.IGNORECASE)]
for idx in matches[:10]:
    print("--- Match at index", idx, "---")
    print(html[max(0, idx-100):min(len(html), idx+500)])
