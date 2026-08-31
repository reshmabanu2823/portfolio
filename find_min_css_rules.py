css_path = 'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css/nothin-preprod.webflow.6a0c501c42b9751b78a9d1a3.ecf8efd0e.opt.min.css'
with open(css_path, 'r', encoding='utf-8') as f:
    c = f.read()

import re
for target in ['img-work', 'work_item', 'title-work', 'short-p-work', 'works-word', 'work_list', 'titile-section-work']:
    matches = re.findall(r'(\.[^{}]*' + target + r'[^{}]*\{[^{}]*\})', c)
    print(f"=== {target} ({len(matches)} matches) ===")
    for m in matches[:5]:
        print(m[:200])
