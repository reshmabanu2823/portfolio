import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

for k in ['merguez', 'ballon', 'img-glitch-w']:
    matches = [m.start() for m in re.finditer(k, c)]
    print(f'{k}: {len(matches)} matches')
    for pos in matches:
        print(c[max(0, pos-40):min(len(c), pos+120)])
        print('---')
