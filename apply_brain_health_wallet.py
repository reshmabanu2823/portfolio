import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Lgm card with Brain Health Interactive Wallet
old_lgm_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item"><h2 line="" class="title-work">Lgm</h2><p line="" class="short-p-work">Swiss clarity for French engineering\.</p><a href="/works/lgm" class="work-link w-inline-block">.*?</a></div>'

new_brain_health_block = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">Brain Health</h2>
  <p line="" class="short-p-work">Cognitive Assessment &amp; Clinical Analytics Platform.</p>
  <a href="/works/brain-health" class="work-link w-inline-block wallet-work-link" onclick="openBrainHealthGallery(event); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer; width: 100%;">
    <div class="wallet-deck-wrapper" style="position: relative; width: 100%; aspect-ratio: 1600 / 947; perspective: 1200px; padding: 10px 0;">
      <!-- Card 1: Left Fanning Wing -->
      <div class="wallet-card wallet-card-left" style="position: absolute; inset: 0; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 20px 45px rgba(0,0,0,0.8); border: 1px solid rgba(255,255,255,0.14); transform: rotate(-5deg) translateY(-2px) translateX(-6px) scale(0.97); transform-origin: bottom center; z-index: 1; transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.55s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
        <img src="/assets/work/brain_health_1.webp" loading="eager" alt="Brain Health — Patient Assessment" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
      </div>
      <!-- Card 2: Right Fanning Wing -->
      <div class="wallet-card wallet-card-right" style="position: absolute; inset: 0; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 24px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transform: rotate(5deg) translateY(-2px) translateX(6px) scale(0.97); transform-origin: bottom center; z-index: 2; transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.55s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
        <img src="/assets/work/brain_health_2.webp" loading="eager" alt="Brain Health — Analytics & Progress" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
      </div>
      <!-- Card 3: Main Front Card -->
      <div class="wallet-card wallet-card-main" style="position: absolute; inset: 0; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 30px 60px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.18); transform: rotate(0deg) scale(1); transform-origin: bottom center; z-index: 3; transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.55s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
        <img src="/assets/work/brain_health_3.webp" loading="eager" alt="Brain Health — Cognitive Health Platform" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        <!-- Explore More Hover Overlay -->
        <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.7) 100%); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); opacity: 0; display: flex; align-items: center; justify-content: center; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none;">
          <div class="explore-btn-pill" style="display: inline-flex; align-items: center; gap: 10px; padding: 14px 28px; border-radius: 40px; background: rgba(255, 255, 255, 0.96); color: #000000; font-size: 15px; font-weight: 500; letter-spacing: -0.01em; box-shadow: 0 20px 40px rgba(0,0,0,0.6); transform: translateY(8px) scale(0.96); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
            <span>Explore Deck (3 Screens)</span>
            <svg width="15" height="12" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.5 1.5L14 6L9.5 10.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M1 6H13.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </a>
</div>'''

matches = re.findall(old_lgm_pattern, html, flags=re.DOTALL)
print(f"Found {len(matches)} matches for Lgm card")

html = re.sub(old_lgm_pattern, new_brain_health_block, html, flags=re.DOTALL)

# Add wallet hover animation CSS & gallery modal
wallet_css_and_gallery = '''
/* Wallet Opening Effect on Hover */
.wallet-work-link:hover .wallet-card-left {
  transform: rotate(-11deg) translateX(-26%) translateY(-14px) scale(0.97) !important;
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 35px rgba(255,255,255,0.1) !important;
  border-color: rgba(255,255,255,0.3) !important;
  z-index: 2 !important;
}

.wallet-work-link:hover .wallet-card-right {
  transform: rotate(11deg) translateX(26%) translateY(-14px) scale(0.97) !important;
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 35px rgba(255,255,255,0.1) !important;
  border-color: rgba(255,255,255,0.3) !important;
  z-index: 2 !important;
}

.wallet-work-link:hover .wallet-card-main {
  transform: rotate(0deg) translateY(-22px) scale(1.03) !important;
  box-shadow: 0 50px 100px rgba(0,0,0,0.98), 0 0 40px rgba(66, 133, 244, 0.25) !important;
  border-color: rgba(255,255,255,0.4) !important;
  z-index: 5 !important;
}

.wallet-work-link:hover .explore-more-overlay {
  opacity: 1 !important;
}

.wallet-work-link:hover .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
'''

# Insert in style block
html = html.replace('/* Hover: Lift card UP and show smooth overlay */', wallet_css_and_gallery + '\n/* Hover: Lift card UP and show smooth overlay */')

# Add Gallery Modal and JS before </body>
gallery_modal_html = '''
<!-- Brain Health Gallery Modal Lightbox -->
<div id="brainHealthGalleryModal" style="position: fixed; inset: 0; background: rgba(0, 0, 0, 0.9); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); z-index: 99999; display: none; align-items: center; justify-content: center; padding: 24px; opacity: 0; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
  <div style="position: absolute; inset: 0; cursor: pointer;" onclick="closeBrainHealthGallery()"></div>
  <div id="brainHealthGalleryContainer" style="position: relative; width: 100%; max-width: 1100px; aspect-ratio: 1600/947; background: #0c1012; border-radius: 16px; overflow: hidden; box-shadow: 0 40px 100px rgba(0,0,0,0.95); border: 1px solid rgba(255,255,255,0.18); z-index: 2; transform: scale(0.95); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1); display: flex; align-items: center; justify-content: center;">
    <button onclick="closeBrainHealthGallery()" style="position: absolute; top: 18px; right: 18px; width: 42px; height: 42px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 18px; line-height: 1; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)'; this.style.transform='scale(1.08)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)'; this.style.transform='scale(1)';">✕</button>
    <button onclick="prevGalleryImage()" style="position: absolute; left: 18px; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)';">❮</button>
    <button onclick="nextGalleryImage()" style="position: absolute; right: 18px; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)';">❯</button>
    
    <img id="galleryMainImage" src="/assets/work/brain_health_3.webp" style="width: 100%; height: 100%; object-fit: contain; display: block; transition: opacity 0.3s ease;"/>
    
    <div id="galleryIndicator" style="position: absolute; bottom: 18px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 10;">
      <span class="dot-ind" onclick="setGalleryImage(0)" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer; transition: all 0.2s ease;"></span>
      <span class="dot-ind" onclick="setGalleryImage(1)" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer; transition: all 0.2s ease;"></span>
      <span class="dot-ind" onclick="setGalleryImage(2)" style="width: 24px; height: 10px; border-radius: 6px; background: #ffffff; cursor: pointer; transition: all 0.2s ease;"></span>
    </div>
  </div>
</div>

<script>
const brainHealthImages = [
  '/assets/work/brain_health_1.webp',
  '/assets/work/brain_health_2.webp',
  '/assets/work/brain_health_3.webp'
];
let currentGalleryIdx = 2;

function updateGalleryDisplay() {
  const img = document.getElementById('galleryMainImage');
  const dots = document.querySelectorAll('.dot-ind');
  if (img) img.src = brainHealthImages[currentGalleryIdx];
  dots.forEach((dot, idx) => {
    if (idx === currentGalleryIdx) {
      dot.style.width = '24px';
      dot.style.borderRadius = '6px';
      dot.style.background = '#ffffff';
    } else {
      dot.style.width = '10px';
      dot.style.borderRadius = '50%';
      dot.style.background = 'rgba(255,255,255,0.4)';
    }
  });
}

function openBrainHealthGallery(e) {
  if (e) e.preventDefault();
  currentGalleryIdx = 2;
  updateGalleryDisplay();
  const modal = document.getElementById('brainHealthGalleryModal');
  const container = document.getElementById('brainHealthGalleryContainer');
  if (modal) {
    modal.style.display = 'flex';
    setTimeout(() => {
      modal.style.opacity = '1';
      if (container) container.style.transform = 'scale(1)';
    }, 20);
  }
}

function closeBrainHealthGallery() {
  const modal = document.getElementById('brainHealthGalleryModal');
  const container = document.getElementById('brainHealthGalleryContainer');
  if (modal) {
    modal.style.opacity = '0';
    if (container) container.style.transform = 'scale(0.95)';
    setTimeout(() => {
      modal.style.display = 'none';
    }, 350);
  }
}

function nextGalleryImage() {
  currentGalleryIdx = (currentGalleryIdx + 1) % brainHealthImages.length;
  updateGalleryDisplay();
}

function prevGalleryImage() {
  currentGalleryIdx = (currentGalleryIdx - 1 + brainHealthImages.length) % brainHealthImages.length;
  updateGalleryDisplay();
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeBrainHealthGallery();
  if (document.getElementById('brainHealthGalleryModal')?.style.display === 'flex') {
    if (e.key === 'ArrowRight') nextGalleryImage();
    if (e.key === 'ArrowLeft') prevGalleryImage();
  }
});
</script>
'''

html = html.replace('</body>', gallery_modal_html + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Create standalone fallback page for brain-health and lgm
works_dir = os.path.join(WORKSPACE, 'works')
www_works_dir = os.path.join(WORKSPACE, 'www.noth.in', 'works')

brain_health_page_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Brain Health Platform | Reshma Banu</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #000; color: #fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 40px 20px; }
    .back-btn { position: fixed; top: 24px; left: 24px; display: inline-flex; align-items: center; gap: 8px; color: #fff; text-decoration: none; font-size: 14px; padding: 10px 18px; border-radius: 30px; background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.15); transition: all 0.2s ease; z-index: 100; }
    .back-btn:hover { background: rgba(255,255,255,0.2); transform: translateX(-3px); }
    .gallery-grid { display: flex; flex-direction: column; gap: 32px; width: 100%; max-width: 1100px; margin-top: 40px; }
    .img-card { width: 100%; border-radius: 16px; overflow: hidden; background: #111; box-shadow: 0 30px 70px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.14); }
    .img-card img { width: 100%; height: auto; display: block; }
    h1 { font-size: 28px; font-weight: 500; margin-bottom: 8px; text-align: center; }
    p { color: rgba(255,255,255,0.6); font-size: 15px; text-align: center; }
  </style>
</head>
<body>
  <a href="/www.noth.in/index.html#works" class="back-btn">← Back to Portfolio</a>
  <h1>Brain Health Platform</h1>
  <p>Cognitive Assessment, Clinical Workflows & Analytics Dashboard</p>
  <div class="gallery-grid">
    <div class="img-card"><img src="/assets/work/brain_health_3.webp" alt="Brain Health Overview"/></div>
    <div class="img-card"><img src="/assets/work/brain_health_2.webp" alt="Brain Health Analytics"/></div>
    <div class="img-card"><img src="/assets/work/brain_health_1.webp" alt="Brain Health Assessment"/></div>
  </div>
</body>
</html>'''

for p in [os.path.join(works_dir, 'brain-health.html'), os.path.join(works_dir, 'lgm.html'),
         os.path.join(www_works_dir, 'brain-health.html'), os.path.join(www_works_dir, 'lgm.html')]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(brain_health_page_html)

print("Applied interactive Wallet Form for Brain Health with full 3-card fanning animation and modal!")
