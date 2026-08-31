import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="work-link')
end_idx = c.find('</a>', idx)
print(c[idx-50:end_idx+10])
