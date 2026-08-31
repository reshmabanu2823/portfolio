import re

with open('www.noth.in/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Search for "A living instrument" or "aurbse"
for match in re.finditer(r'(?:aurbse|living instrument|title-work|short-p-work)', c, re.IGNORECASE):
    pos = match.start()
    print(f"Match '{match.group(0)}' at pos {pos}:")
    print(c[max(0, pos-200):min(len(c), pos+400)])
    print("-" * 50)
