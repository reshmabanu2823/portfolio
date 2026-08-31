import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('class="loader-img-w"')
print("Context around loader-img-w:")
print(html[idx-100:idx+3500])
