import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
main_js_path = os.path.join(WORKSPACE, 'nothinv1.netlify.app', 'main.js')
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

# 1. Fix main.js
with open(main_js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the bad gA.prototype additions at the end
if 'gA.prototype._initRegisteredRevealVideo' in js:
    # Cut off everything after the original main.js end
    idx = js.find('gA.prototype._initRegisteredRevealVideo')
    js = js[:idx].rstrip() + '\n'

# Remove _initRegisteredRevealVideo(), from gA constructor if present
js = js.replace('this._initRegisteredRevealVideo(),this._buildCanvas()', 'this._buildCanvas()')

# Ensure class gA has clean _updateLiveRevealCanvas or standard render loop
with open(main_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed nothinv1.netlify.app/main.js successfully!")

# 2. Update www.noth.in/index.html with the exact requested video src
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace video-hero-bg src with http://localhost:5234/reshma_banu_hero_3d.mp4
new_video_tag = '<video src="http://localhost:5234/reshma_banu_hero_3d.mp4" autoplay="true" loop="" muted="" playsinline="" crossorigin="anonymous" class="video-hero-bg video-hero-bg"></video>'

html = re.sub(
    r'<video[^>]*class="video-hero-bg[^"]*"[^>]*></video>',
    new_video_tag,
    html
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated www.noth.in/index.html with new video source!")
