import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the fullscreen background video from .section-w
content = re.sub(
    r'<video[^>]*class="video-hero-bg[^"]*"[^>]*></video>',
    r'<!-- background video removed for pure white hero layout -->',
    content
)

# 2. In .nothin-hero-w, replace the static SVG with the seamless 3D typography video element
hero_video_element = '''<div class="nothin-hero-w">
  <video src="/reshma_banu_hero_3d.mp4" autoplay="true" loop="true" muted="true" playsinline="true" crossorigin="anonymous" class="nothin-hero-3d-video" style="width: 100%; height: auto; aspect-ratio: 2679.8 / 294; display: block; object-fit: contain; background: #ffffff; pointer-events: none; border: none; outline: none;"></video>
</div>'''

content = re.sub(
    r'<div class="nothin-hero-w">\s*<svg[^>]*class="nothin-hero-svg">.*?</svg>\s*</div>',
    hero_video_element,
    content,
    flags=re.DOTALL
)

# Also handle if already modified
if '<video src="/reshma_banu_hero_3d.mp4"' not in content:
    content = re.sub(
        r'<div class="nothin-hero-w">.*?</div>',
        hero_video_element,
        content,
        count=1,
        flags=re.DOTALL
    )

# 3. Add CSS overrides in <head> to ensure pure white background and no leaking canvas
css_override = '''
<style id="hero-3d-perfect-integration">
  .section-w, .section.hero-home, .container.hero-home, .nothin-hero-w {
    background-color: #ffffff !important;
    background: #ffffff !important;
  }
  .section-w canvas {
    display: none !important;
  }
  .video-hero-bg {
    display: none !important;
  }
  .nothin-hero-svg {
    display: none !important;
  }
  .nothin-hero-w {
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  .nothin-hero-3d-video {
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 2679.8 / 294 !important;
    display: block !important;
    object-fit: contain !important;
    background: #ffffff !important;
    background-color: #ffffff !important;
  }
</style>
</head>'''

if 'id="hero-3d-perfect-integration"' not in content:
    content = content.replace('</head>', css_override, 1)
else:
    content = re.sub(r'<style id="hero-3d-perfect-integration">.*?</style>', css_override.replace('</head>', ''), content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied hero typography fix in www.noth.in/index.html!")
