import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="studio"')
end_idx = html.find('<section class="section formes-w">', idx)
if end_idx == -1:
    end_idx = html.find('formes-w', idx)

studio_markup = html[idx-100:end_idx]
with open(os.path.join(WORKSPACE, 'studio_markup_dump.html'), 'w', encoding='utf-8') as f:
    f.write(studio_markup)

print("Saved studio section markup dump!")
