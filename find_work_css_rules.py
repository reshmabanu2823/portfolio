import os
import re

css_dir = 'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css'
for f in os.listdir(css_dir):
    if f.endswith('.css'):
        p = os.path.join(css_dir, f)
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"=== {f} ===")
        for rule in ['.img-work-w', '.work_item', '.title-work', '.short-p-work', '.works-word', '.work_list', '.works-word-w']:
            for m in re.finditer(re.escape(rule) + r'[^\{]*\{[^\}]*\}', content):
                print(m.group(0))
