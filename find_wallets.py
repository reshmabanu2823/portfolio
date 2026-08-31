import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the project wallets section
idx = html.find('Smart Medication Schedule')
if idx != -1:
    print("Found 'Smart Medication Schedule' at index", idx)
    print(html[idx-300:idx+1500])
else:
    print("Not found by 'Smart Medication Schedule', searching 'Medicine'...")
    matches = [m.start() for m in re.finditer(r'Medicine|Brain', html, flags=re.IGNORECASE)]
    for m in matches[:5]:
        print(html[m-100:m+400])
