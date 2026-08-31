import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

forms_idx = html.find('Forms follow')
print("Context around 'Forms follow' (400 chars before and 400 chars after):")
print(html[max(0, forms_idx-400):forms_idx+400])
