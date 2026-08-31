import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# 1. Update main.js
main_js_path = os.path.join(WORKSPACE, 'nothinv1.netlify.app', 'main.js')
if os.path.exists(main_js_path):
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # In main.js, find pp array and imgH
    # Replace imgH:"43.125rem" with auto or matching 26.875rem
    old_pp = r'imgH:"43\.125rem"'
    new_pp = r'imgH:"auto"'
    js = re.sub(old_pp, new_pp, js)
    
    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js pp array!")

# 2. Update HTML with robust CSS fixes for headers and work cards
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace or enhance the Works CSS block
works_style_block = '''
<!-- Works Section Layout & Clean Flow Fixes -->
<style>
/* Section Works clean header & grid flow */
.section.works {
  position: relative;
  z-index: 10;
  padding-top: 60px;
}

.section.works .works-word-w {
  position: relative !important;
  display: block !important;
  margin-bottom: 28px !important;
  z-index: 2;
  clear: both;
}

.section.works .titile-section-work {
  position: relative !important;
  display: block !important;
  margin-bottom: 48px !important;
  clear: both;
  z-index: 2;
}

.section.works .titile-section-work .h3-style {
  position: relative !important;
  display: block !important;
  font-size: 2rem;
  line-height: 1.25;
  color: #ffffff;
  margin: 0;
}

/* Individual Work Item Flow */
.work_list_w {
  position: relative !important;
  width: 100%;
}

.work_list {
  position: relative !important;
  width: 100%;
}

.work_item {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  margin-bottom: 40px !important;
}

.work_item .title-work {
  position: relative !important;
  top: auto !important;
  left: auto !important;
  right: auto !important;
  bottom: auto !important;
  font-size: 0.85rem !important;
  font-weight: 500 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.12em !important;
  color: rgba(255, 255, 255, 0.6) !important;
  margin: 0 0 6px 0 !important;
  display: block !important;
  transform: none !important;
}

.work_item .short-p-work {
  position: relative !important;
  top: auto !important;
  left: auto !important;
  right: auto !important;
  bottom: auto !important;
  font-size: 1.65rem !important;
  font-weight: 400 !important;
  line-height: 1.25 !important;
  color: #ffffff !important;
  margin: 0 0 16px 0 !important;
  display: block !important;
  transform: none !important;
}

.work_item .work-link {
  position: relative !important;
  width: 100% !important;
  display: block !important;
}

.work_item .img-work-w {
  position: relative !important;
  width: 100% !important;
  height: auto !important;
  max-height: none !important;
  aspect-ratio: 16 / 9.5 !important;
  border-radius: 14px !important;
  overflow: hidden !important;
  background: #0c1012 !important;
  box-shadow: 0 25px 50px rgba(0,0,0,0.85) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
}

.work_item .img-work {
  position: relative !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: top center !important;
  display: block !important;
}

/* Hover overlay and interaction */
.work-link:hover .explore-more-overlay {
  opacity: 1 !important;
}
.work-link:hover .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
.work-link:hover .img-work {
  transform: scale(1.03) !important;
  filter: brightness(0.92) !important;
}
.work-link:hover .img-work-w {
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 40px rgba(255,255,255,0.08) !important;
  border-color: rgba(255,255,255,0.3) !important;
}
</style>
'''

# Update the style block in HTML
if '<!-- Works Section Layout & Clean Flow Fixes -->' in html:
    html = re.sub(r'<!-- Works Section Layout & Clean Flow Fixes -->.*?</style>', works_style_block.strip(), html, flags=re.DOTALL)
else:
    html = re.sub(r'<!-- Hover Styles & Video Modal Lightbox -->\s*<style>.*?</style>', works_style_block.strip(), html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied Works clean layout and card sizing fixes!")
