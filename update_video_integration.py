import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update hero background video
content = re.sub(
    r'<video[^>]*class="video-hero-bg[^"]*"[^>]*>',
    r'<video src="/reshma_banu_3d_typography.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="video-hero-bg video-hero-bg">',
    content
)

# Update showreel video
content = re.sub(
    r'<video[^>]*class="showreel-light"[^>]*>',
    r'<video src="/reshma_banu_3d_typography.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="showreel-light">',
    content
)

# Update studio video
content = re.sub(
    r'<video[^>]*class="video-sticky"[^>]*>',
    r'<video src="/reshma_banu_3d_typography.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="video-sticky">',
    content
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated video elements in www.noth.in/index.html!")
