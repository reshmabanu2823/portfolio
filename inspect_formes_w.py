import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('class="formes-w"')
print("Context around formes-w:")
print(html[idx-100:idx+2500])
