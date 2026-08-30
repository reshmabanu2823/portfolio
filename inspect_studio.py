import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="studio"')
if idx == -1:
    idx = c.find('The Studio')
print("Found at index:", idx)
print(c[idx-100:idx+2500])
