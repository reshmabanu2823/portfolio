import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_cards_markup = '''<div class="img-glitch-w" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;">
  <!-- Card 1: Google Cloud -->
  <div class="cert-card cert-card-1" style="position: absolute; top: 14%; left: 11%; width: clamp(330px, 33.5vw, 560px); pointer-events: auto; z-index: 2;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 14px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.24); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px) scale(1.02)'; this.style.boxShadow='0 45px 80px rgba(0,0,0,0.98), 0 0 35px rgba(255,255,255,0.18)'; this.style.borderColor='rgba(255,255,255,0.45)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6)'; this.style.borderColor='rgba(255,255,255,0.24)';">
      <img src="/assets/certificates/cert_google_cloud.png" alt="Google Cloud Certified - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 14px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 2: Intel Cybersecurity -->
  <div class="cert-card cert-card-2" style="position: absolute; top: 14%; right: 11%; width: clamp(330px, 33.5vw, 560px); pointer-events: auto; z-index: 3;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 14px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.24); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px) scale(1.02)'; this.style.boxShadow='0 45px 80px rgba(0,0,0,0.98), 0 0 35px rgba(255,255,255,0.18)'; this.style.borderColor='rgba(255,255,255,0.45)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6)'; this.style.borderColor='rgba(255,255,255,0.24)';">
      <img src="/assets/certificates/cert_cybersecurity_intel.png" alt="Intel Cybersecurity Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 14px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 3: MERN Stack -->
  <div class="cert-card cert-card-3" style="position: absolute; bottom: 14%; left: 11%; width: clamp(330px, 33.5vw, 560px); pointer-events: auto; z-index: 4;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 14px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.24); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px) scale(1.02)'; this.style.boxShadow='0 45px 80px rgba(0,0,0,0.98), 0 0 35px rgba(255,255,255,0.18)'; this.style.borderColor='rgba(255,255,255,0.45)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6)'; this.style.borderColor='rgba(255,255,255,0.24)';">
      <img src="/assets/certificates/cert_mern_stack.png" alt="MERN Stack Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 14px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 4: NodeJS -->
  <div class="cert-card cert-card-4" style="position: absolute; bottom: 14%; right: 11%; width: clamp(330px, 33.5vw, 560px); pointer-events: auto; z-index: 5;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 14px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.24); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px) scale(1.02)'; this.style.boxShadow='0 45px 80px rgba(0,0,0,0.98), 0 0 35px rgba(255,255,255,0.18)'; this.style.borderColor='rgba(255,255,255,0.45)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.92), 0 4px 14px rgba(0,0,0,0.6)'; this.style.borderColor='rgba(255,255,255,0.24)';">
      <img src="/assets/certificates/cert_nodejs.png" alt="NodeJS Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 14px; margin: 0; padding: 0;"/>
    </div>
  </div>
</div>'''

pattern = r'<div class="img-glitch-w".*?<!-- Card 4: NodeJS -->.*?</div>\s*</div>\s*</div>'
html = re.sub(pattern, new_cards_markup, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully increased the size of all 4 certificate images with balanced alignment!")
