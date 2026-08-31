with open('www.noth.in/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

head_end = c.find('</head>')
head = c[:head_end]

import re
print("Styles and Links in head:")
for link in re.finditer(r'<link[^>]*rel="stylesheet"[^>]*>', head):
    print("Link:", link.group(0))

for style in re.finditer(r'<style[^>]*>(.*?)</style>', head, re.DOTALL):
    print("Style length:", len(style.group(1)))
    # print first 200 chars
    print("Style preview:", style.group(1)[:200].strip())
