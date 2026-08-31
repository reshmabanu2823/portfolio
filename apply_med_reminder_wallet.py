import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Haptify card with Medicine Reminder Fanned Wallet Stack
old_haptify_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item"><h2 line="" class="title-work">Haptify</h2>.*?</a></div>'

new_med_reminder_card = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">Medicine Reminder</h2>
  <p line="" class="short-p-work">Smart Medication Schedule &amp; Adherence Companion.</p>
  <a href="/works/medicine-reminder" class="work-link w-inline-block" onclick="openMedReminderGallery(event); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer; width: 100%;">
    <div class="img-work-w med-reminder-wallet-vignette" style="position: relative; width: 100%; aspect-ratio: 16 / 9.5; border-radius: 14px; overflow: hidden; background: radial-gradient(circle at center, #171d24 0%, #080a0d 100%); box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
      
      <!-- Fanned Cards Stack in Wallet Form -->
      <div class="wallet-fanned-stack" style="position: absolute; inset: 0; width: 100%; height: 100%; perspective: 1200px; display: flex; align-items: center; justify-content: center;">
        
        <!-- Card 1: Left Fanned Card -->
        <div class="wallet-card-item card-left" style="position: absolute; width: 73%; height: 75%; left: 8%; top: 12%; border-radius: 10px; overflow: hidden; background: #0c1012; box-shadow: 0 15px 35px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.16); transform: rotate(-4.5deg) translateY(4px) translateX(-20px); transform-origin: bottom left; z-index: 1; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/medicine_reminder_1.webp" loading="eager" alt="Medicine Reminder — Schedule Overview" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
        <!-- Card 2: Right Fanned Card -->
        <div class="wallet-card-item card-right" style="position: absolute; width: 73%; height: 75%; right: 8%; top: 12%; border-radius: 10px; overflow: hidden; background: #0c1012; box-shadow: 0 18px 40px rgba(0,0,0,0.88); border: 1px solid rgba(255,255,255,0.16); transform: rotate(4.5deg) translateY(4px) translateX(20px); transform-origin: bottom right; z-index: 2; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/medicine_reminder_2.webp" loading="eager" alt="Medicine Reminder — Prescription Logs" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
        <!-- Card 3: Center Foreground Hero Card -->
        <div class="wallet-card-item card-center" style="position: absolute; width: 78%; height: 80%; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(0deg); border-radius: 12px; overflow: hidden; background: #0c1012; box-shadow: 0 25px 60px rgba(0,0,0,0.95); border: 1px solid rgba(255,255,255,0.22); z-index: 3; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/medicine_reminder_3.webp" loading="eager" alt="Medicine Reminder — Patient Dashboard" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
      </div>
      
      <!-- Explore More Hover Overlay -->
      <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.65) 100%); backdrop-filter: blur(3px); -webkit-backdrop-filter: blur(3px); opacity: 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 24px; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none; z-index: 20;">
        <div class="explore-btn-pill" style="display: inline-flex; align-items: center; gap: 10px; padding: 12px 24px; border-radius: 40px; background: rgba(255, 255, 255, 0.96); color: #000000; font-size: 14px; font-weight: 500; letter-spacing: -0.01em; box-shadow: 0 20px 40px rgba(0,0,0,0.7); transform: translateY(8px) scale(0.96); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
          <span>Explore Deck (9 Screens)</span>
          <svg width="14" height="11" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.5 1.5L14 6L9.5 10.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M1 6H13.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round"/>
          </svg>
        </div>
      </div>
      
    </div>
  </a>
</div>'''

html = re.sub(old_haptify_pattern, new_med_reminder_card, html, flags=re.DOTALL)

# Add CSS rules for Medicine Reminder Wallet Vignette
med_css = '''
/* Specific Hover Interactions for Medicine Reminder Wallet Vignette */
.med-reminder-wallet-vignette .wallet-card-item {
  pointer-events: auto;
  cursor: pointer;
}

.med-reminder-wallet-vignette .card-left:hover {
  z-index: 15 !important;
  transform: rotate(0deg) translateY(-14px) translateX(-30px) scale(1.05) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.98), 0 0 30px rgba(255,255,255,0.18) !important;
  border-color: rgba(255,255,255,0.45) !important;
}

.med-reminder-wallet-vignette .card-right:hover {
  z-index: 15 !important;
  transform: rotate(0deg) translateY(-14px) translateX(30px) scale(1.05) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.98), 0 0 30px rgba(255,255,255,0.18) !important;
  border-color: rgba(255,255,255,0.45) !important;
}

.med-reminder-wallet-vignette .card-center:hover {
  z-index: 15 !important;
  transform: translate(-50%, -50%) translateY(-14px) scale(1.05) !important;
  box-shadow: 0 40px 85px rgba(0,0,0,0.98), 0 0 35px rgba(52, 168, 83, 0.3) !important;
  border-color: rgba(255,255,255,0.5) !important;
}

.work-link:hover .med-reminder-wallet-vignette {
  transform: translateY(-8px) scale(1.01) !important;
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 35px rgba(255,255,255,0.12) !important;
  border-color: rgba(255,255,255,0.32) !important;
}

.work-link:hover .med-reminder-wallet-vignette .explore-more-overlay {
  opacity: 1 !important;
}

.work-link:hover .med-reminder-wallet-vignette .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
'''

if '/* Specific Hover Interactions for Medicine Reminder Wallet Vignette */' not in html:
    html = html.replace('/* Hover: Lift card UP and show smooth overlay */', med_css + '\n/* Hover: Lift card UP and show smooth overlay */')

# Add 9-screen Gallery Modal for Medicine Reminder before </body>
med_gallery_modal = '''
<!-- Medicine Reminder Gallery Modal Lightbox -->
<div id="medReminderGalleryModal" style="position: fixed; inset: 0; background: rgba(0, 0, 0, 0.9); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); z-index: 99999; display: none; align-items: center; justify-content: center; padding: 24px; opacity: 0; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
  <div style="position: absolute; inset: 0; cursor: pointer;" onclick="closeMedReminderGallery()"></div>
  <div id="medReminderGalleryContainer" style="position: relative; width: 100%; max-width: 1100px; aspect-ratio: 1600/960; background: #0c1012; border-radius: 16px; overflow: hidden; box-shadow: 0 40px 100px rgba(0,0,0,0.95); border: 1px solid rgba(255,255,255,0.18); z-index: 2; transform: scale(0.95); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1); display: flex; align-items: center; justify-content: center;">
    <button onclick="closeMedReminderGallery()" style="position: absolute; top: 18px; right: 18px; width: 42px; height: 42px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 18px; line-height: 1; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)'; this.style.transform='scale(1.08)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)'; this.style.transform='scale(1)';">✕</button>
    <button onclick="prevMedImage()" style="position: absolute; left: 18px; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)';">❮</button>
    <button onclick="nextMedImage()" style="position: absolute; right: 18px; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.3); color: #ffffff; font-size: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.2s ease;" onmouseenter="this.style.background='rgba(255,255,255,0.25)';" onmouseleave="this.style.background='rgba(0,0,0,0.7)';">❯</button>
    
    <img id="medGalleryMainImage" src="/assets/work/medicine_reminder_3.webp" style="width: 100%; height: 100%; object-fit: contain; display: block; transition: opacity 0.3s ease;"/>
    
    <div id="medGalleryIndicator" style="position: absolute; bottom: 18px; left: 50%; transform: translateX(-50%); display: flex; gap: 6px; z-index: 10;">
      <!-- Generated dynamically in JS -->
    </div>
  </div>
</div>

<script>
const medReminderImages = [
  '/assets/work/medicine_reminder_1.webp',
  '/assets/work/medicine_reminder_2.webp',
  '/assets/work/medicine_reminder_3.webp',
  '/assets/work/medicine_reminder_4.webp',
  '/assets/work/medicine_reminder_5.webp',
  '/assets/work/medicine_reminder_6.webp',
  '/assets/work/medicine_reminder_7.webp',
  '/assets/work/medicine_reminder_8.webp',
  '/assets/work/medicine_reminder_9.webp'
];
let currentMedIdx = 2;

function renderMedDots() {
  const container = document.getElementById('medGalleryIndicator');
  if (!container) return;
  container.innerHTML = '';
  medReminderImages.forEach((_, idx) => {
    const dot = document.createElement('span');
    dot.onclick = () => setMedImage(idx);
    dot.style.cursor = 'pointer';
    dot.style.transition = 'all 0.2s ease';
    if (idx === currentMedIdx) {
      dot.style.width = '20px';
      dot.style.height = '8px';
      dot.style.borderRadius = '4px';
      dot.style.background = '#ffffff';
    } else {
      dot.style.width = '8px';
      dot.style.height = '8px';
      dot.style.borderRadius = '50%';
      dot.style.background = 'rgba(255,255,255,0.4)';
    }
    container.appendChild(dot);
  });
}

function updateMedDisplay() {
  const img = document.getElementById('medGalleryMainImage');
  if (img) img.src = medReminderImages[currentMedIdx];
  renderMedDots();
}

function setMedImage(idx) {
  currentMedIdx = idx;
  updateMedDisplay();
}

function openMedReminderGallery(e) {
  if (e) e.preventDefault();
  currentMedIdx = 2;
  updateMedDisplay();
  const modal = document.getElementById('medReminderGalleryModal');
  const container = document.getElementById('medReminderGalleryContainer');
  if (modal) {
    modal.style.display = 'flex';
    setTimeout(() => {
      modal.style.opacity = '1';
      if (container) container.style.transform = 'scale(1)';
    }, 20);
  }
}

function closeMedReminderGallery() {
  const modal = document.getElementById('medReminderGalleryModal');
  const container = document.getElementById('medReminderGalleryContainer');
  if (modal) {
    modal.style.opacity = '0';
    if (container) container.style.transform = 'scale(0.95)';
    setTimeout(() => {
      modal.style.display = 'none';
    }, 350);
  }
}

function nextMedImage() {
  currentMedIdx = (currentMedIdx + 1) % medReminderImages.length;
  updateMedDisplay();
}

function prevMedImage() {
  currentMedIdx = (currentMedIdx - 1 + medReminderImages.length) % medReminderImages.length;
  updateMedDisplay();
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeMedReminderGallery();
  if (document.getElementById('medReminderGalleryModal')?.style.display === 'flex') {
    if (e.key === 'ArrowRight') nextMedImage();
    if (e.key === 'ArrowLeft') prevMedImage();
  }
});
</script>
'''

html = html.replace('</body>', med_gallery_modal + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Create standalone fallback page for medicine-reminder and haptify
works_dir = os.path.join(WORKSPACE, 'works')
www_works_dir = os.path.join(WORKSPACE, 'www.noth.in', 'works')

med_page_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Medicine Reminder | Reshma Banu</title>
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
  <h1>Medicine Reminder</h1>
  <p>Smart Medication Schedule & Adherence Companion (9 Screens)</p>
  <div class="gallery-grid">
''' + '\n'.join([f'    <div class="img-card"><img src="/assets/work/medicine_reminder_{i+1}.webp" alt="Screen {i+1}"/></div>' for i in range(9)]) + '''
  </div>
</body>
</html>'''

for p in [os.path.join(works_dir, 'medicine-reminder.html'), os.path.join(works_dir, 'haptify.html'),
         os.path.join(www_works_dir, 'medicine-reminder.html'), os.path.join(www_works_dir, 'haptify.html')]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(med_page_html)

print("Applied scoped Fanned Cards in Wallet treatment specifically to Medicine Reminder vignette!")
