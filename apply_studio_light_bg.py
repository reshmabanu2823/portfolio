import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the studio section markup to ensure clear classes and clean card contents
old_hero_markup = r'<div class="badge-card-hero".*?</div>\s*</div>\s*</div>'

new_hero_markup = '''<div class="badge-card-hero" style="flex: 1; height: 100%; border-radius: 16px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 20px 45px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.03); padding: 24px 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; box-sizing: border-box; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;">
      <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(66,133,244,0.03) 0%, transparent 60%); pointer-events: none;"></div>
      <img src="/assets/certificates/badge_gcp_computing.png" alt="Google Cloud Computing Certificate - Reshma Banu" loading="lazy" style="width: 100%; max-width: 160px; max-height: 160px; height: auto; object-fit: contain; display: block; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.1)); margin-bottom: 14px;"/>
      <div class="hero-card-title" style="color: #111827; font-size: 16px; font-weight: 600; letter-spacing: -0.01em; margin-bottom: 4px;">Google Cloud Certified</div>
      <div class="hero-card-subtitle" style="color: #64748b; font-size: 12px; letter-spacing: 0.02em; text-transform: uppercase; font-weight: 500;">Computing Foundations</div>
    </div>
  </div>'''

# Replace hero card
html = re.sub(r'<div class="badge-card-hero".*?</div>\s*</div>\s*(?=\s*<!-- Right 2x2)', new_hero_markup, html, flags=re.DOTALL)

# 2. Add scoped Studio Light Background CSS
studio_light_css = '''
/* =========================================================
   STUDIO SECTION LIGHT HARMONIZED BACKGROUND & SHADOWS
   ========================================================= */
#studio.section.info-img {
  position: relative !important;
  background: radial-gradient(ellipse at 50% 40%, #f7f8fa 0%, #ebedf2 55%, #dfe3e8 100%) !important;
  color: #111822 !important;
  overflow: hidden !important;
  z-index: 5 !important;
}

/* Smooth Top Transition from Video Hero */
#studio.section.info-img::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 160px;
  background: linear-gradient(180deg, #000000 0%, rgba(0,0,0,0.82) 25%, rgba(0,0,0,0.3) 65%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

/* Smooth Bottom Transition to Forms Follow Perspective */
#studio.section.info-img::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 180px;
  background: linear-gradient(0deg, #000000 0%, rgba(0,0,0,0.85) 25%, rgba(0,0,0,0.3) 65%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

/* Text Contrast inside Studio Section */
#studio .info-w > div:first-child {
  color: #111822 !important;
  font-weight: 500 !important;
}

#studio .text-block-7 {
  color: #1a202c !important;
}

/* Left Hero Shield Card on Light Surface */
#studio .badge-card-hero {
  background: #ffffff !important;
  border: 1px solid rgba(0,0,0,0.08) !important;
  box-shadow: 0 20px 45px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.03) !important;
}

#studio .badge-card-hero:hover {
  transform: translateY(-8px) scale(1.02) !important;
  border-color: rgba(66, 133, 244, 0.45) !important;
  box-shadow: 0 30px 60px rgba(0,0,0,0.12), 0 0 35px rgba(66, 133, 244, 0.15) !important;
}

/* Right 4 Badge Cards on Light Surface */
#studio .badge-card-item {
  background: #ffffff !important;
  border: 1px solid rgba(0,0,0,0.08) !important;
  box-shadow: 0 16px 36px rgba(0,0,0,0.07), 0 3px 10px rgba(0,0,0,0.03) !important;
}

#studio .badge-card-item:hover {
  transform: translateY(-6px) scale(1.03) !important;
  box-shadow: 0 28px 56px rgba(0,0,0,0.12), 0 0 25px rgba(66, 133, 244, 0.15) !important;
  border-color: rgba(66, 133, 244, 0.4) !important;
}
'''

# Insert in style block
html = html.replace('/* Specific Hover Interactions for Medicine Reminder Wallet Vignette */', studio_light_css + '\n/* Specific Hover Interactions for Medicine Reminder Wallet Vignette */')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied light harmonized studio background, smooth top/bottom fades, and soft card shadows!")
