import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('img-glitch-w')
end_idx = c.find('</section>', idx)
print(c[idx:end_idx+20])
