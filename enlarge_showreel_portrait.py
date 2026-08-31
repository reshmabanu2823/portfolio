import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update .video-showreel-w in section showreel with larger portrait and video
old_showreel_markup = r'<div class="video-showreel-w".*?</section>'

new_showreel_markup = '''<div class="video-showreel-w" style="display: flex; align-items: center; justify-content: space-between; gap: clamp(24px, 4vw, 56px); flex-wrap: wrap;">
      <div class="video-showreel-flip p-m" style="flex: 1 1 300px; max-width: 440px;">
        <div delay="0.2" line="">( The step aside )</div>
        <div delay="0.2" line="" class="text-block-2">In a world of infinite images, the rare thing is clarity. Images defend ideas, experiences shift perception, and brands change how people see the world.</div>
      </div>
      <div class="video-showreel-media-side" style="display: flex; align-items: center; gap: clamp(20px, 2.5vw, 36px); flex: 1 1 auto; justify-content: flex-end; flex-wrap: wrap;">
        <!-- Enlarged Portrait on the LEFT side of the video -->
        <div class="showreel-portrait-w" style="position: relative; width: clamp(280px, 28vw, 460px); aspect-ratio: 1 / 1; border-radius: 18px; overflow: hidden; box-shadow: 0 25px 55px rgba(0,0,0,0.1), 0 4px 14px rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.06); flex-shrink: 0; background: #f8fafc; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;" onmouseenter="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 35px 70px rgba(0,0,0,0.14)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 25px 55px rgba(0,0,0,0.1), 0 4px 14px rgba(0,0,0,0.04)';">
          <img src="/assets/portrait/reshma-portrait.jpg" alt="Reshma Banu" loading="eager" style="width: 100%; height: 100%; object-fit: contain; display: block; border-radius: 18px;" />
        </div>
        <!-- Video Container on the right -->
        <div class="video-showreel-full-w" style="position: relative; width: clamp(320px, 32vw, 520px); aspect-ratio: 16 / 10; border-radius: 18px; overflow: hidden; box-shadow: 0 25px 55px rgba(0,0,0,0.1), 0 4px 14px rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.06); flex-shrink: 0;">
          <video src="/generated_video_showreel.mp4" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="showreel-light" style="width: 100%; height: 100%; object-fit: cover; display: block;"></video>
        </div>
      </div>
    </div></div></div></section>'''

html = re.sub(old_showreel_markup, new_showreel_markup, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully enlarged portrait image with balanced alignment and full uncropped dimensions!")
