import os
import re

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.css'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                c = fh.read()
            for clz in ['img-block-left', 'img-block-right-w', 'img-block-grid', 'img-block-left-w']:
                if clz in c:
                    print(f'{p} has {clz}')
                    for m in re.finditer(clz, c):
                        pos = m.start()
                        print(c[max(0, pos-20):min(len(c), pos+150)])
                        print('---')
