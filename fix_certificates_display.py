import os
import shutil
import re
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

cert_dir = os.path.join(WORKSPACE, 'assets', 'certificates')
www_cert_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'certificates')
os.makedirs(cert_dir, exist_ok=True)
os.makedirs(www_cert_dir, exist_ok=True)

# 1. Copy exact full original PNGs
certs = [
    ('cert_cybersecurity_intel.png', 'media_1788101554789.png'),
    ('cert_mern_stack.png', 'media_1788101556872.png'),
    ('cert_google_cloud.png', 'media_1788101577161.png'),
    ('cert_nodejs.png', 'media_1788101706661.png')
]

for out_name, src_name in certs:
    src_p = os.path.join(UPLOAD_DIR, src_name)
    shutil.copyfile(src_p, os.path.join(cert_dir, out_name))
    shutil.copyfile(src_p, os.path.join(www_cert_dir, out_name))
    print(f"Copied full PNG {out_name} -> {os.path.getsize(src_p)/1024:.1f} KB")

# 2. Update HTML with full uncropped display
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace img-glitch-w block with uncropped certificates
old_glitch_img = r'<div class="img-glitch-w">.*?</div></div></div></section>'

new_glitch_img = '''<div class="img-glitch-w" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;">
  <div class="cert-card-1" style="position: absolute; top: 18%; left: 6%; width: 38vw; max-width: 580px; min-width: 320px; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.2); pointer-events: auto; z-index: 2; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_google_cloud.png" alt="Google Cloud Certified - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-2" style="position: absolute; top: 28%; right: 6%; width: 40vw; max-width: 600px; min-width: 320px; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.2); pointer-events: auto; z-index: 3; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_cybersecurity_intel.png" alt="Intel Cybersecurity Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-3" style="position: absolute; bottom: 14%; left: 10%; width: 36vw; max-width: 540px; min-width: 300px; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.2); pointer-events: auto; z-index: 4; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_mern_stack.png" alt="MERN Stack Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
  <div class="cert-card-4" style="position: absolute; bottom: 8%; right: 12%; width: 36vw; max-width: 540px; min-width: 300px; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.85); border: 1px solid rgba(255,255,255,0.2); pointer-events: auto; z-index: 5; transition: transform 0.4s ease, box-shadow 0.4s ease;">
    <img src="/assets/certificates/cert_nodejs.png" alt="NodeJS Certification - Reshma Banu" loading="lazy" style="width: 100% !important; height: auto !important; max-height: none !important; display: block !important; object-fit: contain !important; border-radius: 12px; margin: 0; padding: 0;"/>
  </div>
</div></div></div></section>'''

html = re.sub(old_glitch_img, new_glitch_img, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated www.noth.in/index.html with full uncropped PNG certificate images!")
