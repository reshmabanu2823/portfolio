import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="studio"')
end_idx = html.find('</section>', idx)
studio_html = html[idx:end_idx+10]
print(f"Studio section length: {len(studio_html)}")

# Print with safe encoding
import sys
sys.stdout.buffer.write(studio_html.encode('utf-8'))
