import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace In_Cognita image card with video card
old_incognita_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item"><h2 line="" class="title-work">In_Cognita</h2><p line="" class="short-p-work">Seize the unexpected: the invisible, made visible\.</p><a href="/works/in-cognita" class="work-link w-inline-block">.*?</a></div>'

new_incognita_block = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">In_Cognita</h2>
  <p line="" class="short-p-work">Seize the unexpected: the invisible, made visible.</p>
  <a href="/works/in-cognita" class="work-link w-inline-block" data-video-url="/incognita_video.mp4" onclick="openWorkVideo(event, this); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
    <div class="img-work-w" style="position: relative; width: 100%; aspect-ratio: 2496 / 1478; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
      <video src="/incognita_video.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="img-work" style="position: absolute; top: 0; left: 0; width: 100% !important; height: 100% !important; object-fit: cover !important; object-position: center !important; display: block !important; transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;"></video>
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

matches = re.findall(old_incognita_pattern, html, flags=re.DOTALL)
print(f"Found {len(matches)} matches for In_Cognita card")

html = re.sub(old_incognita_pattern, new_incognita_block, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Create standalone fallback pages for in-cognita
works_dir = os.path.join(WORKSPACE, 'works')
www_works_dir = os.path.join(WORKSPACE, 'www.noth.in', 'works')

incognita_page_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>In_Cognita | Reshma Banu</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #000; color: #fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 20px; }
    .back-btn { position: fixed; top: 24px; left: 24px; display: inline-flex; align-items: center; gap: 8px; color: #fff; text-decoration: none; font-size: 14px; padding: 10px 18px; border-radius: 30px; background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.15); transition: all 0.2s ease; z-index: 100; }
    .back-btn:hover { background: rgba(255,255,255,0.2); transform: translateX(-3px); }
    .video-card { width: 100%; max-width: 1100px; aspect-ratio: 2496/1478; border-radius: 16px; overflow: hidden; background: #111; box-shadow: 0 40px 100px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.15); margin-bottom: 24px; }
    video { width: 100%; height: 100%; object-fit: contain; background: #000; }
    h1 { font-size: 24px; font-weight: 500; margin-bottom: 6px; }
    p { color: rgba(255,255,255,0.6); font-size: 14px; }
  </style>
</head>
<body>
  <a href="/www.noth.in/index.html#works" class="back-btn">← Back to Portfolio</a>
  <div class="video-card">
    <video src="/incognita_video.mp4" controls autoplay playsinline></video>
  </div>
  <h1>In_Cognita</h1>
  <p>Seize the unexpected: the invisible, made visible.</p>
</body>
</html>'''

for p in [os.path.join(works_dir, 'in-cognita.html'), os.path.join(works_dir, 'in-cognita'),
         os.path.join(www_works_dir, 'in-cognita.html'), os.path.join(www_works_dir, 'in-cognita')]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(incognita_page_html)

print("Successfully replaced In_Cognita image with video card, hover rise, and standalone showcase!")
