import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace img-glitch-w with tightly and beautifully clustered certificates
old_glitch_img = r'<div class="img-glitch-w"[^>]*>.*?</div></div></div></section>'

new_glitch_img = '''<div class="img-glitch-w" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;">
  <div class="cert-card-1" style="position: absolute; top: 22%; left: 26%; width: 23vw; max-width: 360px; min-width: 240px; border-radius: 10px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 2; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_google_cloud.png" alt="Google Cloud Certified - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 10px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-2" style="position: absolute; top: 22%; right: 26%; width: 23vw; max-width: 360px; min-width: 240px; border-radius: 10px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 3; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_cybersecurity_intel.png" alt="Intel Cybersecurity Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 10px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-3" style="position: absolute; bottom: 22%; left: 27%; width: 22vw; max-width: 340px; min-width: 230px; border-radius: 10px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 4; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_mern_stack.png" alt="MERN Stack Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 10px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-4" style="position: absolute; bottom: 22%; right: 27%; width: 22vw; max-width: 340px; min-width: 230px; border-radius: 10px; overflow: hidden; box-shadow: 0 25px 45px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.22); pointer-events: auto; z-index: 5; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_nodejs.png" alt="NodeJS Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 10px; margin: 0; padding: 0;"/>
  </div>
</div></div></div></section>'''

html = re.sub(old_glitch_img, new_glitch_img, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Clustered certificates closer to each other successfully!")
