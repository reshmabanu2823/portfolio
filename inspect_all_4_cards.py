import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx1 = html.find('<!-- Card 1: Google Cloud -->')
idx2 = html.find('</section>', idx1)
print(html[idx1-200:idx2])
