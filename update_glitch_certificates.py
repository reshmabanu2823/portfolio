import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace img-glitch-w with the enlarged, tighter, hover-rise certificate layout
old_glitch_img = r'<div class="img-glitch-w"[^>]*>.*?</div></div></div></section>'

new_glitch_img = '''<div class="img-glitch-w" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;">
  <!-- Card 1: Google Cloud -->
  <div class="cert-card cert-card-1" style="position: absolute; top: 20%; left: 19%; width: 27vw; max-width: 420px; min-width: 280px; pointer-events: auto; z-index: 2;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 40px 70px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.15)'; this.style.borderColor='rgba(255,255,255,0.4)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 25px 45px rgba(0,0,0,0.9)'; this.style.borderColor='rgba(255,255,255,0.22)';">
      <img src="/assets/certificates/cert_google_cloud.png" alt="Google Cloud Certified - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 2: Intel Cybersecurity -->
  <div class="cert-card cert-card-2" style="position: absolute; top: 20%; right: 19%; width: 27vw; max-width: 420px; min-width: 280px; pointer-events: auto; z-index: 3;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 40px 70px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.15)'; this.style.borderColor='rgba(255,255,255,0.4)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 25px 45px rgba(0,0,0,0.9)'; this.style.borderColor='rgba(255,255,255,0.22)';">
      <img src="/assets/certificates/cert_cybersecurity_intel.png" alt="Intel Cybersecurity Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 3: MERN Stack -->
  <div class="cert-card cert-card-3" style="position: absolute; bottom: 20%; left: 19%; width: 27vw; max-width: 420px; min-width: 280px; pointer-events: auto; z-index: 4;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 40px 70px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.15)'; this.style.borderColor='rgba(255,255,255,0.4)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 25px 45px rgba(0,0,0,0.9)'; this.style.borderColor='rgba(255,255,255,0.22)';">
      <img src="/assets/certificates/cert_mern_stack.png" alt="MERN Stack Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
    </div>
  </div>

  <!-- Card 4: NodeJS -->
  <div class="cert-card cert-card-4" style="position: absolute; bottom: 20%; right: 19%; width: 27vw; max-width: 420px; min-width: 280px; pointer-events: auto; z-index: 5;">
    <div class="cert-card-inner" style="width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease; cursor: pointer;" onmouseenter="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 40px 70px rgba(0,0,0,0.95), 0 0 30px rgba(255,255,255,0.15)'; this.style.borderColor='rgba(255,255,255,0.4)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 25px 45px rgba(0,0,0,0.9)'; this.style.borderColor='rgba(255,255,255,0.22)';">
      <img src="/assets/certificates/cert_nodejs.png" alt="NodeJS Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
    </div>
  </div>
</div></div></div></section>'''

html = re.sub(old_glitch_img, new_glitch_img, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated floating certificate cards with enlarged size, tighter centering, and clean hover-rise!")
