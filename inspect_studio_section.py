import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="studio"')
if idx != -1:
    print("Found studio section (1500 chars):")
    print(html[idx:idx+1500])
