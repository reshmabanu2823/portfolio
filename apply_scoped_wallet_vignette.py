import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Target the Brain Health / LGM card specifically
old_brain_health_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">\s*<h2 line="" class="title-work">Brain Health</h2>.*?</a>\s*</div>'

new_brain_health_card = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">Brain Health</h2>
  <p line="" class="short-p-work">Cognitive Assessment &amp; Clinical Analytics Platform.</p>
  <a href="/works/brain-health" class="work-link w-inline-block" onclick="openBrainHealthGallery(event); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer; width: 100%;">
    <div class="img-work-w brain-health-wallet-vignette" style="position: relative; width: 100%; aspect-ratio: 16 / 9.5; border-radius: 14px; overflow: hidden; background: radial-gradient(circle at center, #141b22 0%, #080a0d 100%); box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;">
      
      <!-- Fanned Cards Stack in Wallet Form -->
      <div class="wallet-fanned-stack" style="position: absolute; inset: 0; width: 100%; height: 100%; perspective: 1200px; display: flex; align-items: center; justify-content: center;">
        
        <!-- Card 1: Left Fanned Card (Patient Assessment) -->
        <div class="wallet-card-item card-left" style="position: absolute; width: 73%; height: 75%; left: 8%; top: 12%; border-radius: 10px; overflow: hidden; background: #0c1012; box-shadow: 0 15px 35px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.16); transform: rotate(-4.5deg) translateY(4px) translateX(-20px); transform-origin: bottom left; z-index: 1; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/brain_health_1.webp" loading="eager" alt="Brain Health — Patient Assessment" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
        <!-- Card 2: Right Fanned Card (Clinical Analytics) -->
        <div class="wallet-card-item card-right" style="position: absolute; width: 73%; height: 75%; right: 8%; top: 12%; border-radius: 10px; overflow: hidden; background: #0c1012; box-shadow: 0 18px 40px rgba(0,0,0,0.88); border: 1px solid rgba(255,255,255,0.16); transform: rotate(4.5deg) translateY(4px) translateX(20px); transform-origin: bottom right; z-index: 2; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/brain_health_2.webp" loading="eager" alt="Brain Health — Analytics & Progress" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
        <!-- Card 3: Center Foreground Hero Card (Overview Platform) -->
        <div class="wallet-card-item card-center" style="position: absolute; width: 78%; height: 80%; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(0deg); border-radius: 12px; overflow: hidden; background: #0c1012; box-shadow: 0 25px 60px rgba(0,0,0,0.95); border: 1px solid rgba(255,255,255,0.22); z-index: 3; transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);">
          <img src="/assets/work/brain_health_3.webp" loading="eager" alt="Brain Health — Cognitive Health Platform" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        </div>
        
      </div>
      
      <!-- Explore More Hover Overlay -->
      <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.65) 100%); backdrop-filter: blur(3px); -webkit-backdrop-filter: blur(3px); opacity: 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 24px; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none; z-index: 20;">
        <div class="explore-btn-pill" style="display: inline-flex; align-items: center; gap: 10px; padding: 12px 24px; border-radius: 40px; background: rgba(255, 255, 255, 0.96); color: #000000; font-size: 14px; font-weight: 500; letter-spacing: -0.01em; box-shadow: 0 20px 40px rgba(0,0,0,0.7); transform: translateY(8px) scale(0.96); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
          <span>Explore Deck (3 Screens)</span>
          <svg width="14" height="11" viewBox="0 0 15 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.5 1.5L14 6L9.5 10.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M1 6H13.5" stroke="#000000" stroke-width="1.8" stroke-linecap="round"/>
          </svg>
        </div>
      </div>
      
    </div>
  </a>
</div>'''

html = re.sub(old_brain_health_pattern, new_brain_health_card, html, flags=re.DOTALL)

# 2. Add specific hover CSS for the fanned wallet card stack
wallet_css = '''
/* Specific Hover Interactions for Brain Health Wallet Vignette */
.brain-health-wallet-vignette .wallet-card-item {
  pointer-events: auto;
  cursor: pointer;
}

.brain-health-wallet-vignette .card-left:hover {
  z-index: 15 !important;
  transform: rotate(0deg) translateY(-14px) translateX(-30px) scale(1.05) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.98), 0 0 30px rgba(255,255,255,0.18) !important;
  border-color: rgba(255,255,255,0.45) !important;
}

.brain-health-wallet-vignette .card-right:hover {
  z-index: 15 !important;
  transform: rotate(0deg) translateY(-14px) translateX(30px) scale(1.05) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.98), 0 0 30px rgba(255,255,255,0.18) !important;
  border-color: rgba(255,255,255,0.45) !important;
}

.brain-health-wallet-vignette .card-center:hover {
  z-index: 15 !important;
  transform: translate(-50%, -50%) translateY(-14px) scale(1.05) !important;
  box-shadow: 0 40px 85px rgba(0,0,0,0.98), 0 0 35px rgba(66, 133, 244, 0.3) !important;
  border-color: rgba(255,255,255,0.5) !important;
}

.work-link:hover .brain-health-wallet-vignette {
  transform: translateY(-8px) scale(1.01) !important;
  box-shadow: 0 40px 80px rgba(0,0,0,0.95), 0 0 35px rgba(255,255,255,0.12) !important;
  border-color: rgba(255,255,255,0.32) !important;
}

.work-link:hover .brain-health-wallet-vignette .explore-more-overlay {
  opacity: 1 !important;
}

.work-link:hover .brain-health-wallet-vignette .explore-btn-pill {
  transform: translateY(0px) scale(1) !important;
}
'''

# Update or insert into style block
if '/* Specific Hover Interactions for Brain Health Wallet Vignette */' not in html:
    html = html.replace('/* Hover: Lift card UP and show smooth overlay */', wallet_css + '\n/* Hover: Lift card UP and show smooth overlay */')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied scoped Fanned Cards in Wallet treatment specifically to Brain Health vignette!")
