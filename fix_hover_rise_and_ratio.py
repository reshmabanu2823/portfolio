import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the work-link markup for Utopia
old_work_link = r'<a href="/works/utopia" class="work-link w-inline-block".*?</a>'

new_work_link = '''<a href="/works/utopia" class="work-link w-inline-block" data-video-url="" onclick="openWorkVideo(event, this); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
  <div class="img-work-w" style="position: relative; width: 100%; aspect-ratio: 1024 / 608; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
    <img src="/assets/work/musicify-screenshot.webp" loading="eager" alt="Musicify — music streaming app dashboard" sizes="100vw" srcset="/assets/work/musicify-screenshot-p-500.webp 500w, /assets/work/musicify-screenshot-p-800.webp 800w, /assets/work/musicify-screenshot-p-1080.webp 1080w, /assets/work/musicify-screenshot.webp 1600w" class="img-work" style="position: absolute; top: 0; left: 0; width: 100% !important; height: 100% !important; object-fit: cover !important; object-position: top center !important; display: block !important; transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;"/>
    <!-- Explore More Hover Overlay -->
    <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.7) 100%); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); opacity: 0; display: flex; align-items: center; justify-content: center; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none;">
      <div class="explore-btn-pill" style="display: inline-flex; align-items: center; gap: 10px; padding: 14px 28px; border-radius: 40px; background: rgba(255, 255, 255, 0.96); color: #000000; font-size: 15px; font-weight: 500; letter-spacing: -0.01em; box-shadow: 0 20px 40px rgba(0,0,0,0.6); transform: translateY(8px) scale(0.96); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
        <span>Explore More</span>
        <svg width="15" height="12" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M9.5 1.5L14 6L9.5 10.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M1 6H13.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round"/>
        </svg>
      </div>
    </div>
  </div>
</a>'''

html = re.sub(old_work_link, new_work_link, html, count=1, flags=re.DOTALL)

# 2. Update Hover Styles
old_style_block = r'<!-- Works Section Layout & Clean Flow Fixes -->\s*<style>.*?</style>'

new_style_block = '''<!-- Works Section Layout & Clean Flow Fixes -->
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

.work_item .work-link .cursor-work {
  display: none !important;
}

.work_item .img-work-w {
  position: relative !important;
  width: 100% !important;
  height: auto !important;
  aspect-ratio: 1024 / 608 !important;
  border-radius: 14px !important;
  overflow: hidden !important;
  background: #0c1012 !important;
  box-shadow: 0 25px 50px rgba(0,0,0,0.85) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease !important;
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
  transform: none !important;
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease !important;
}

/* Hover: Lift card UP and show smooth overlay */
.work-link:hover .img-work-w {
  transform: translateY(-8px) scale(1.01) !important;
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 35px rgba(255,255,255,0.12) !important;
  border-color: rgba(255,255,255,0.32) !important;
}

.work-link:hover .img-work {
  transform: scale(1.02) !important;
  filter: brightness(0.92) !important;
}

.work-link:hover .explore-more-overlay {
  opacity: 1 !important;
}

.work-link:hover .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
</style>'''

html = re.sub(old_style_block, new_style_block, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied smooth hover rise and full edge-to-edge original ratio!")
