import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the work item link and img-work container
old_work_link = r'<a href="/works/utopia" class="work-link w-inline-block">.*?</a>'

new_work_link = '''<a href="/works/utopia" class="work-link w-inline-block" data-video-url="" onclick="openWorkVideo(event, this); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
  <div class="img-work-w" style="position: relative; width: 100%; aspect-ratio: 16 / 9.5; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 30px 60px rgba(0,0,0,0.8); border: 1px solid rgba(255,255,255,0.14);">
    <img src="/assets/work/musicify-screenshot.webp" loading="eager" alt="Musicify — music streaming app dashboard" sizes="100vw" srcset="/assets/work/musicify-screenshot-p-500.webp 500w, /assets/work/musicify-screenshot-p-800.webp 800w, /assets/work/musicify-screenshot-p-1080.webp 1080w, /assets/work/musicify-screenshot.webp 1600w" class="img-work" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;"/>
    <!-- Explore More Hover Overlay -->
    <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.45) 0%, rgba(0,0,0,0.72) 100%); backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px); opacity: 0; display: flex; align-items: center; justify-content: center; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none;">
      <div class="explore-btn-pill" style="display: inline-flex; align-items: center; gap: 10px; padding: 14px 28px; border-radius: 40px; background: rgba(255, 255, 255, 0.96); color: #000000; font-size: 15px; font-weight: 500; letter-spacing: -0.01em; box-shadow: 0 20px 40px rgba(0,0,0,0.6); transform: translateY(8px) scale(0.96); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
        <span>Explore More</span>
        <svg width="15" height="12" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M9.5 1.5L14 6L9.5 10.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M1 6H13.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round"/>
        </svg>
      </div>
    </div>
  </div>
  <div class="cursor-work"><div>explore</div><div class="w-embed"><svg width="14" height="10" viewBox="0 0 14 10" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M8.60254 0.353516L13.1188 4.86981L8.60254 9.3861" stroke="white"/>
<line y1="5.01562" x2="13.1188" y2="5.01562" stroke="white"/>
</svg>
</div></div></a>'''

html = re.sub(old_work_link, new_work_link, html, flags=re.DOTALL)

# 2. Add Hover CSS and Modal before </body>
modal_and_css = '''
<!-- Hover Styles & Video Modal Lightbox -->
<style>
.work-link:hover .explore-more-overlay {
  opacity: 1 !important;
}
.work-link:hover .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
.work-link:hover .img-work {
  transform: scale(1.03) !important;
  filter: brightness(0.92) !important;
}
.work-link:hover .img-work-w {
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 40px rgba(255,255,255,0.08) !important;
  border-color: rgba(255,255,255,0.3) !important;
}
</style>

<div id="workVideoModal" style="position: fixed; inset: 0; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); z-index: 99999; display: none; align-items: center; justify-content: center; padding: 24px; opacity: 0; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
  <div style="position: absolute; inset: 0; cursor: pointer;" onclick="closeWorkVideo()"></div>
  <div id="workVideoContainer" style="position: relative; width: 100%; max-width: 1040px; aspect-ratio: 16/9; background: #000000; border-radius: 16px; overflow: hidden; box-shadow: 0 40px 100px rgba(0,0,0,0.95); border: 1px solid rgba(255,255,255,0.18); z-index: 2; transform: scale(0.95); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
    <button onclick="closeWorkVideo()" style="position: absolute; top: 18px; right: 18px; width: 42px; height: 42px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 18px; line-height: 1; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)'; this.style.transform='scale(1.08)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)'; this.style.transform='scale(1)';">✕</button>
    <video id="modalVideoPlayer" controls autoplay playsinline style="width: 100%; height: 100%; object-fit: cover; display: block;"></video>
  </div>
</div>

<script>
function openWorkVideo(e, el) {
  if (e) e.preventDefault();
  // ONE-LINE CHANGE: Set default video url here or pass via data-video-url attribute
  const DEFAULT_VIDEO_URL = '/generated_video_1.mp4';
  const videoSrc = (el && el.getAttribute('data-video-url')) ? el.getAttribute('data-video-url') : DEFAULT_VIDEO_URL;
  
  const modal = document.getElementById('workVideoModal');
  const container = document.getElementById('workVideoContainer');
  const player = document.getElementById('modalVideoPlayer');
  
  if (modal && player) {
    player.src = videoSrc;
    modal.style.display = 'flex';
    setTimeout(() => {
      modal.style.opacity = '1';
      if (container) container.style.transform = 'scale(1)';
      player.play().catch(() => {});
    }, 20);
  }
}

function closeWorkVideo() {
  const modal = document.getElementById('workVideoModal');
  const container = document.getElementById('workVideoContainer');
  const player = document.getElementById('modalVideoPlayer');
  
  if (modal) {
    modal.style.opacity = '0';
    if (container) container.style.transform = 'scale(0.95)';
    if (player) player.pause();
    setTimeout(() => {
      modal.style.display = 'none';
      if (player) player.src = '';
    }, 350);
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeWorkVideo();
});
</script>
'''

if 'id="workVideoModal"' not in html:
    html = html.replace('</body>', modal_and_css + '\n</body>')
else:
    # Replace existing modal block
    html = re.sub(r'<!-- Hover Styles & Video Modal Lightbox -->.*?</body>', modal_and_css + '\n</body>', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied clean vignette framing, Explore More hover overlay, and Video Modal Lightbox!")
