import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Brain Health block with Stepped Wallet Card Slot Assembly
old_brain_health_pattern = r'<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item"><h2 line="" class="title-work">Brain Health</h2>.*?</a></div>'

new_brain_health_block = '''<div id="w-node-_4052a9ed-bc85-74d6-2f8d-4f251e3cf60d-78a9d1a3" role="listitem" class="work_item w-dyn-item">
  <h2 line="" class="title-work">Brain Health</h2>
  <p line="" class="short-p-work">Cognitive Assessment &amp; Clinical Analytics Platform.</p>
  <a href="/works/brain-health" class="work-link w-inline-block wallet-work-link" onclick="openBrainHealthGallery(event); return false;" style="display: block; position: relative; text-decoration: none; cursor: pointer; width: 100%;">
    <div class="wallet-deck-wrapper" style="position: relative; width: 100%; aspect-ratio: 1600 / 1060; border-radius: 16px; perspective: 1200px; padding-top: 10px; padding-bottom: 60px;">
      
      <!-- Wallet Card 1: Top / Back Slot (Slotted & peeking at top) -->
      <div class="wallet-card wallet-card-slot1" style="position: absolute; top: 0px; left: 4%; width: 92%; aspect-ratio: 1600 / 947; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 12px 28px rgba(0,0,0,0.75); border: 1px solid rgba(255,255,255,0.1); filter: brightness(0.72); z-index: 1; transition: all 0.55s cubic-bezier(0.16, 1, 0.3, 1);">
        <img src="/assets/work/brain_health_1.webp" loading="eager" alt="Brain Health — Patient Assessment" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
      </div>
      
      <!-- Wallet Card 2: Middle Slot (Slotted & peeking in middle) -->
      <div class="wallet-card wallet-card-slot2" style="position: absolute; top: 28px; left: 2%; width: 96%; aspect-ratio: 1600 / 947; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 18px 38px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.14); filter: brightness(0.86); z-index: 2; transition: all 0.55s cubic-bezier(0.16, 1, 0.3, 1);">
        <img src="/assets/work/brain_health_2.webp" loading="eager" alt="Brain Health — Analytics & Progress" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
      </div>
      
      <!-- Wallet Card 3: Front Slot (Full front view) -->
      <div class="wallet-card wallet-card-slot3" style="position: absolute; top: 56px; left: 0px; width: 100%; aspect-ratio: 1600 / 947; border-radius: 14px; overflow: hidden; background: #0c1012; box-shadow: 0 28px 65px rgba(0,0,0,0.92); border: 1px solid rgba(255,255,255,0.18); filter: brightness(1); z-index: 3; transition: all 0.55s cubic-bezier(0.16, 1, 0.3, 1);">
        <img src="/assets/work/brain_health_3.webp" loading="eager" alt="Brain Health — Cognitive Health Platform" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
        
        <!-- Explore More Hover Overlay -->
        <div class="explore-more-overlay" style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.38) 0%, rgba(0,0,0,0.68) 100%); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); opacity: 0; display: flex; align-items: center; justify-content: center; transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1); pointer-events: none;">
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

html = re.sub(old_brain_health_pattern, new_brain_health_block, html, flags=re.DOTALL)

# Update Hover CSS for Wallet Slots Opening
old_wallet_css = r'/\* Wallet Opening Effect on Hover \*/.*?(?=/\* Hover: Lift card UP)'

new_wallet_css = '''/* Wallet Opening Effect on Hover */
.wallet-work-link:hover .wallet-card-slot1 {
  transform: rotate(-10deg) translateX(-30%) translateY(-28px) scale(0.97) !important;
  filter: brightness(1) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.1) !important;
  border-color: rgba(255,255,255,0.3) !important;
  z-index: 4 !important;
}

.wallet-work-link:hover .wallet-card-slot2 {
  transform: rotate(10deg) translateX(30%) translateY(-28px) scale(0.97) !important;
  filter: brightness(1) !important;
  box-shadow: 0 35px 75px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.1) !important;
  border-color: rgba(255,255,255,0.3) !important;
  z-index: 4 !important;
}

.wallet-work-link:hover .wallet-card-slot3 {
  transform: rotate(0deg) translateY(-18px) scale(1.02) !important;
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

html = re.sub(old_wallet_css, new_wallet_css, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Brain Health card assembly to authentic Stepped Wallet Card Look!")
