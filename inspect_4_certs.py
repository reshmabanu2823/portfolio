import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('cert_google_cloud.png')
print(html[idx-400:idx+2600])
