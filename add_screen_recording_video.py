import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Locate Brain Health item ending
brain_idx = html.find('openBrainHealthGallery')
end_of_brain_item = html.find('</div>', html.find('</a>', brain_idx)) + 6

video_item_markup = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a4" role="listitem" class="work_item w-dyn-item work-video-featured-item" style="grid-column: 1 / -1; width: 100%; margin-top: clamp(24px, 3.5vw, 48px);">
  <h2 line="" class="title-work">Platform Experience &amp; Interaction</h2>
  <p line="" class="short-p-work">Full-fidelity interface walkthrough &amp; screen capture demo.</p>
  <div class="img-work-w" style="position: relative; width: 100%; border-radius: 16px; overflow: hidden; background: #080a0d; box-shadow: 0 30px 65px rgba(0,0,0,0.92); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;">
    <video src="/assets/work/screen_recording_project.mp4" autoplay="true" loop="" muted="" playsinline="true" controls="true" crossorigin="anonymous" style="width: 100%; height: auto; max-height: 85vh; display: block; object-fit: contain; background: #000000;"></video>
  </div>
</div>'''

html = html[:end_of_brain_item] + video_item_markup + html[end_of_brain_item:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added screen recording video below project wallets!")
