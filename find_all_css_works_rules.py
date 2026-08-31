css_files = [
    'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css/nothin-preprod.webflow.6a0c501c42b9751b78a9d1a3.ecf8efd0e.opt.min.css',
    'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css/nothin-preprod.webflow.shared.1ca0c6df4.min.css'
]

import re

for cf in css_files:
    with open(cf, 'r', encoding='utf-8') as f:
        c = f.read()
    print("=" * 60)
    print(cf)
    for term in ['works', 'work_item', 'work_list', 'title-work', 'short-p-work', 'img-work']:
        for m in re.finditer(r'(\.[^{}]*' + term + r'[^{}]*\{[^{}]*\})', c):
            print(m.group(1))
