import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the exact split point
pattern = r'(<section id="studio"[^>]*>.*?</div>\s*</div>\s*</div>)(\s*<div class="space-150 hide-landscape">.*?)(</section>)'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    print("Found exact matching section blocks!")
    studio_light_part = match.group(1)
    forms_part = match.group(2)
    
    print(f"Studio Light Part length: {len(studio_light_part)}")
    print(f"Forms Part length: {len(forms_part)}")
else:
    print("Could not match pattern, checking variations...")
