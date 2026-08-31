import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the two cards
item4_match = re.search(r'(<div id="w-node-[^>]*role="listitem" class="work_item[^"]*">\s*<h2[^>]*class="title-work"[^>]*>Brain Health.*?</div>\s*</div>\s*</a>\s*</div>)', html, flags=re.DOTALL)
item5_match = re.search(r'(<div id="w-node-[^>]*role="listitem" class="work_item[^"]*">\s*<h2[^>]*class="title-work"[^>]*>Medicine Reminder.*?</div>\s*</div>\s*</a>\s*</div>)', html, flags=re.DOTALL)

print("Item 4 found:", bool(item4_match))
print("Item 5 found:", bool(item5_match))
