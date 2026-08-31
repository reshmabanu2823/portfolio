css_files = [
    'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css/nothin-preprod.webflow.6a0c501c42b9751b78a9d1a3.ecf8efd0e.opt.min.css',
    'cdn.prod.website-files.com/6a0c501c42b9751b78a9d1a7/css/nothin-preprod.webflow.shared.1ca0c6df4.min.css'
]

for cf in css_files:
    with open(cf, 'r', encoding='utf-8') as f:
        c = f.read()
    print("=" * 60)
    print(cf, "length:", len(c))
    for term in ['works-word', 'title-work', 'short-p-work', 'img-work-w', 'work_list', 'titile-section']:
        idx = 0
        while True:
            idx = c.find(term, idx)
            if idx == -1:
                break
            start = max(0, idx - 40)
            end = min(len(c), idx + 100)
            print(f"[{term}] at {idx}: {c[start:end]}")
            idx += len(term)
