import os
import shutil
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

# Ensure high quality portrait is copied
original_src = r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788186828395.jpg"
target_dir = os.path.join(WORKSPACE, 'assets', 'portrait')
target_dir_www = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'portrait')
os.makedirs(target_dir, exist_ok=True)
os.makedirs(target_dir_www, exist_ok=True)

shutil.copy(original_src, os.path.join(target_dir, 'reshma-portrait.jpg'))
shutil.copy(original_src, os.path.join(target_dir_www, 'reshma-portrait.jpg'))

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update .video-showreel-w in section showreel
old_showreel_markup = r'<div class="video-showreel-w">.*?</div>\s*</div>\s*</div>\s*</section>'

# Portrait is placed on the LEFT side of the video
new_showreel_markup = '''<div class="video-showreel-w" style="display: flex; align-items: center; justify-content: space-between; gap: clamp(20px, 3vw, 48px); flex-wrap: wrap;">
      <div class="video-showreel-flip p-m" style="flex: 1 1 280px; max-width: 440px;">
        <div delay="0.2" line="">( The step aside )</div>
        <div delay="0.2" line="" class="text-block-2">In a world of infinite images, the rare thing is clarity. Images defend ideas, experiences shift perception, and brands change how people see the world.</div>
      </div>
      <div class="video-showreel-media-side" style="display: flex; align-items: center; gap: clamp(16px, 2vw, 28px); flex: 1 1 auto; justify-content: flex-end; flex-wrap: wrap;">
        <!-- Portrait on the LEFT side of the video -->
        <div class="showreel-portrait-w" style="position: relative; width: clamp(200px, 20vw, 320px); aspect-ratio: 1 / 1; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 45px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); flex-shrink: 0; background: #f8fafc;">
          <img src="/assets/portrait/reshma-portrait.jpg" alt="Reshma Banu" loading="eager" style="width: 100%; height: 100%; object-fit: cover; object-position: center 20%; display: block;" />
        </div>
        <!-- Video Container on the right -->
        <div class="video-showreel-full-w" style="position: relative; width: clamp(260px, 26vw, 420px); aspect-ratio: 16 / 10; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 45px rgba(0,0,0,0.08);">
          <video src="/generated_video_showreel.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="showreel-light" style="width: 100%; height: 100%; object-fit: cover; display: block;"></video>
        </div>
      </div>
    </div></div></div></section>'''

html = re.sub(old_showreel_markup, new_showreel_markup, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully placed portrait on the left side next to the video!")
