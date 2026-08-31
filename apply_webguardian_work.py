import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Aurbse with WebGuardian
old_aurbse_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item"><h2 line="" class="title-work">Aurbse</h2><p line="" class="short-p-work">A living instrument for reading territory\. </p><a href="/works/aurbse" class="work-link w-inline-block">.*?</a></div>'

new_webguardian_block = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">WebGuardian</h2>
  <p line="" class="short-p-work">Clinical Dossier &amp; Consent Engine.</p>
  <a href="/works/webguardian" class="work-link w-inline-block" data-video-url="/webguardian_video.mp4" onclick="openWorkVideo(event, this); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
    <div class="img-work-w" style="position: relative; width: 100%; aspect-ratio: 1024 / 554; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
      <img src="/assets/work/webguardian-screenshot.webp" loading="eager" alt="WebGuardian — Clinical Dossier & Consent Engine" sizes="100vw" srcset="/assets/work/webguardian-screenshot-p-500.webp 500w, /assets/work/webguardian-screenshot-p-800.webp 800w, /assets/work/webguardian-screenshot-p-1080.webp 1080w, /assets/work/webguardian-screenshot.webp 1500w" class="img-work" style="position: absolute; top: 0; left: 0; width: 100% !important; height: 100% !important; object-fit: cover !important; object-position: top center !important; display: block !important; transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;"/>
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
  </a>
</div>'''

matches = re.findall(old_aurbse_pattern, html, flags=re.DOTALL)
print(f"Found {len(matches)} matches for Aurbse card")

html = re.sub(old_aurbse_pattern, new_webguardian_block, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced Aurbse with WebGuardian card, hover rise, and video modal link!")
