import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

matches = [m.start() for m in re.finditer(r'MEDICINE REMINDER|Brain Health|Smart Medication', html, flags=re.IGNORECASE)]
print(f"Found {len(matches)} matches:")
for idx in matches:
    print("--- Match at index", idx, "---")
    print(html[max(0, idx-100):min(len(html), idx+800)])
