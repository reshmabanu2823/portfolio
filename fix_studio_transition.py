import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean up section header and remove overlay divs
multi_stop_bg = "linear-gradient(180deg, rgba(0, 0, 0, 1) 0%, rgba(0, 0, 0, 0.72) 6%, rgba(0, 0, 0, 0.42) 12%, rgba(0, 0, 0, 0.2) 18%, rgba(0, 0, 0, 0.06) 24%, rgba(0, 0, 0, 0) 30%, rgba(0, 0, 0, 0) 72%, rgba(0, 0, 0, 0.06) 78%, rgba(0, 0, 0, 0.2) 84%, rgba(0, 0, 0, 0.45) 90%, rgba(0, 0, 0, 0.75) 95%, rgba(0, 0, 0, 1) 100%), url('/assets/backgrounds/studio-bg-light.jpg') center center / cover no-repeat"

old_section_block_pattern = r'<section id="studio"[^>]*>.*?<div class="container"[^>]*>'
new_section_block = f'<section id="studio" class="section info-img studio-light-section" style="position: relative; background: {multi_stop_bg}; color: #0f172a; overflow: hidden; padding-top: 60px; padding-bottom: 90px;">\n  <div class="container" style="position: relative; z-index: 3;">'

html = re.sub(old_section_block_pattern, new_section_block, html, flags=re.DOTALL)

# 2. Update CSS for Studio Section
studio_css_pattern = r'/\* =========================================================\s*STUDIO SECTION LIGHT HARMONIZED BACKGROUND & SHADOWS\s*========================================================= \*/.*?/\* Specific Hover Interactions for Medicine Reminder Wallet Vignette \*/'

new_studio_css = f'''/* =========================================================
   STUDIO SECTION LIGHT HARMONIZED BACKGROUND & SHADOWS
   ========================================================= */
#studio.section.info-img {{
  position: relative !important;
  background: {multi_stop_bg} !important;
  color: #0f172a !important;
  overflow: hidden !important;
  z-index: 5 !important;
}}

/* Text Contrast inside Studio Section */
#studio .info-w > div:first-child {{
  color: #0f172a !important;
  font-weight: 600 !important;
  text-shadow: 0 1px 2px rgba(255,255,255,0.6) !important;
}}

#studio .text-block-7 {{
  color: #0f172a !important;
  font-weight: 500 !important;
  text-shadow: 0 1px 2px rgba(255,255,255,0.6) !important;
}}

/* Left Hero Shield Card on Light Surface */
#studio .badge-card-hero {{
  background: #ffffff !important;
  border: 1px solid rgba(0,0,0,0.08) !important;
  box-shadow: 0 20px 45px rgba(0,0,0,0.15), 0 4px 12px rgba(0,0,0,0.06) !important;
}}

#studio .badge-card-hero:hover {{
  transform: translateY(-8px) scale(1.02) !important;
  border-color: rgba(66, 133, 244, 0.45) !important;
  box-shadow: 0 32px 65px rgba(0,0,0,0.2), 0 0 35px rgba(66, 133, 244, 0.2) !important;
}}

/* Right 4 Badge Cards on Light Surface */
#studio .badge-card-item {{
  background: #ffffff !important;
  border: 1px solid rgba(0,0,0,0.08) !important;
  box-shadow: 0 20px 40px rgba(0,0,0,0.15), 0 4px 12px rgba(0,0,0,0.06) !important;
}}

#studio .badge-card-item:hover {{
  transform: translateY(-6px) scale(1.03) !important;
  box-shadow: 0 30px 60px rgba(0,0,0,0.2), 0 0 25px rgba(66, 133, 244, 0.2) !important;
  border-color: rgba(66, 133, 244, 0.4) !important;
}}

/* Specific Hover Interactions for Medicine Reminder Wallet Vignette */'''

html = re.sub(studio_css_pattern, new_studio_css, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully removed redundant fade overlays and applied continuous multi-stop transition!")
