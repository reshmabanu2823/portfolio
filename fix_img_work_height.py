import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# 1. Update main.js
main_js_path = os.path.join(WORKSPACE, 'nothinv1.netlify.app', 'main.js')
if os.path.exists(main_js_path):
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Replace height:e?"auto":"100%" with height:"100%"
    js = js.replace('height:e?"auto":"100%"', 'height:"100%"')
    js = js.replace('height:e?"100%":"100%"', 'height:"100%"')
    
    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js image height handling!")

# 2. Update HTML
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update the img-work tag in Utopia / Musicify
old_img_pattern = r'<img\s+src="/assets/work/musicify-screenshot\.webp"[^>]*class="img-work"[^>]*>'

new_img_tag = '<img src="/assets/work/musicify-screenshot.webp" loading="eager" alt="Musicify — music streaming app dashboard" sizes="100vw" srcset="/assets/work/musicify-screenshot-p-500.webp 500w, /assets/work/musicify-screenshot-p-800.webp 800w, /assets/work/musicify-screenshot-p-1080.webp 1080w, /assets/work/musicify-screenshot.webp 1600w" class="img-work" style="position: absolute; top: 0; left: 0; width: 100% !important; height: 100% !important; object-fit: cover !important; object-position: top center !important; display: block !important; transform: translate(0%, -18.9156%); transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;"/>'

html = re.sub(old_img_pattern, new_img_tag, html)

# Update CSS in index.html to ensure .img-work is 100% height and position: absolute inside position: relative container
css_rule = '''.work_item .img-work-w {
  position: relative !important;
  width: 100% !important;
  height: auto !important;
  aspect-ratio: 16 / 9.5 !important;
  border-radius: 14px !important;
  overflow: hidden !important;
  background: #0c1012 !important;
  box-shadow: 0 25px 50px rgba(0,0,0,0.85) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
}

.work_item .img-work {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: top center !important;
  display: block !important;
}'''

# Replace in style block if needed
if '.work_item .img-work {' in html:
    html = re.sub(r'\.work_item \.img-work-w\s*\{[^}]*\}\s*\.work_item \.img-work\s*\{[^}]*\}', css_rule, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully enforced height: 100% on .img-work to eliminate black gap!")
