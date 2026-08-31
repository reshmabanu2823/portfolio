import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the two work items
item4_match = re.search(r'(<div id="w-node-[^>]*role="listitem" class="work_item[^"]*">\s*<h2[^>]*class="title-work"[^>]*>Brain Health.*?</div>\s*</div>\s*</a>\s*</div>)', html, flags=re.DOTALL)
item5_match = re.search(r'(<div id="w-node-[^>]*role="listitem" class="work_item[^"]*">\s*<h2[^>]*class="title-work"[^>]*>Medicine Reminder.*?</div>\s*</div>\s*</a>\s*</div>)', html, flags=re.DOTALL)

if item4_match:
    print("Found Item 4 (Brain Health) length:", len(item4_match.group(1)))
if item5_match:
    print("Found Item 5 (Medicine Reminder) length:", len(item5_match.group(1)))
