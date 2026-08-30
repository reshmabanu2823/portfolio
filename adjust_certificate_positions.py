import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace img-glitch-w with tightly clustered certificates
old_glitch_img = r'<div class="img-glitch-w"[^>]*>.*?</div></div></div></section>'

new_glitch_img = '''<div class="img-glitch-w" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;">
  <div class="cert-card-1" style="position: absolute; top: 18%; left: 16%; width: 31vw; max-width: 450px; min-width: 280px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 2; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_google_cloud.png" alt="Google Cloud Certified - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-2" style="position: absolute; top: 20%; right: 16%; width: 31vw; max-width: 450px; min-width: 280px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 3; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_cybersecurity_intel.png" alt="Intel Cybersecurity Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-3" style="position: absolute; bottom: 16%; left: 19%; width: 29vw; max-width: 420px; min-width: 270px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 4; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_mern_stack.png" alt="MERN Stack Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-4" style="position: absolute; bottom: 18%; right: 19%; width: 29vw; max-width: 420px; min-width: 270px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 5; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_nodejs.png" alt="NodeJS Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
</div></div></div></section>'''

html = re.sub(old_glitch_img, new_glitch_img, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated certificate positions to be closer to each other!")
