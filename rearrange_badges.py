import os
import shutil
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

cert_dir = os.path.join(WORKSPACE, 'assets', 'certificates')
www_cert_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'certificates')

# Copy the 5th badge
src_p = os.path.join(UPLOAD_DIR, 'media_1788110928747.png')
shutil.copyfile(src_p, os.path.join(cert_dir, 'badge_gcp_appdev.png'))
shutil.copyfile(src_p, os.path.join(www_cert_dir, 'badge_gcp_appdev.png'))
print(f"Copied badge_gcp_appdev.png ({os.path.getsize(src_p)/1024:.1f} KB)")

html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Build the interactive, reactive, beautifully arranged badges section
# 1 Main Featured Shield on the left + 2x2 grid of 4 Skill Badges on the right
old_studio_grid = r'<div id="w-node-_8c8bfc91-8576-abe0-d854-49082250bec5-78a9d1a3" class="img-block-grid".*?</div></div></div><div class="space-150 hide-landscape">'

new_studio_grid = '''<div id="w-node-_8c8bfc91-8576-abe0-d854-49082250bec5-78a9d1a3" class="img-block-grid" style="display: grid; grid-template-columns: 1fr 1.6fr; gap: 36px; align-items: stretch; margin-top: 24px;">
  <!-- Left Featured Shield Card -->
  <div parallax-scrub="1" parallax-y="-40" parallax="" id="w-node-_01baddd9-d465-59de-ee3e-5a9211c9095b-78a9d1a3" class="img-block-left" style="display: flex; flex-direction: column;">
    <div class="badge-card-hero" style="flex: 1; border-radius: 16px; background: radial-gradient(circle at 50% 20%, rgba(66, 133, 244, 0.08), rgba(255, 255, 255, 0.02) 70%); border: 1px solid rgba(255,255,255,0.14); box-shadow: 0 30px 60px rgba(0,0,0,0.85); padding: 32px 28px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-8px) scale(1.02)'; this.style.borderColor='rgba(66, 133, 244, 0.5)'; this.style.boxShadow='0 40px 80px rgba(0,0,0,0.95), 0 0 40px rgba(66, 133, 244, 0.25)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(255,255,255,0.14)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.85)';">
      <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 60%); pointer-events: none;"></div>
      <img src="/assets/certificates/badge_gcp_computing.png" alt="Google Cloud Computing Certificate - Reshma Banu" loading="lazy" style="width: 100%; max-width: 220px; height: auto; object-fit: contain; display: block; filter: drop-shadow(0 15px 30px rgba(0,0,0,0.6)); margin-bottom: 20px;"/>
      <div style="color: #ffffff; font-size: 17px; font-weight: 500; letter-spacing: -0.01em; margin-bottom: 6px;">Google Cloud Certified</div>
      <div style="color: rgba(255,255,255,0.55); font-size: 13px; letter-spacing: 0.02em; text-transform: uppercase;">Computing Foundations</div>
    </div>
  </div>

  <!-- Right 2x2 Skill Badges Grid -->
  <div parallax-scrub="2" parallax-y="-20" parallax="" class="img-block-right-w" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; width: 100%;">
    <!-- Badge 1 -->
    <div class="badge-card-item" style="border-radius: 14px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 18px; display: flex; align-items: center; justify-content: center; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(52, 168, 83, 0.5)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.9), 0 0 30px rgba(52, 168, 83, 0.2)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(255,255,255,0.12)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.7)';">
      <img src="/assets/certificates/badge_gcp_security.png" alt="Build a Secure Google Cloud Network - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
    </div>

    <!-- Badge 2 -->
    <div class="badge-card-item" style="border-radius: 14px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 18px; display: flex; align-items: center; justify-content: center; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(66, 133, 244, 0.5)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.9), 0 0 30px rgba(66, 133, 244, 0.2)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(255,255,255,0.12)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.7)';">
      <img src="/assets/certificates/badge_gcp_loadbalancing.png" alt="Implement Load Balancing on Compute Engine - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
    </div>

    <!-- Badge 3 -->
    <div class="badge-card-item" style="border-radius: 14px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 18px; display: flex; align-items: center; justify-content: center; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(251, 188, 5, 0.5)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.9), 0 0 30px rgba(251, 188, 5, 0.2)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(255,255,255,0.12)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.7)';">
      <img src="/assets/certificates/badge_gcp_ml.png" alt="Prepare Data for ML APIs on Google Cloud - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
    </div>

    <!-- Badge 4 (New) -->
    <div class="badge-card-item" style="border-radius: 14px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 18px; display: flex; align-items: center; justify-content: center; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(234, 67, 53, 0.5)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.9), 0 0 30px rgba(234, 67, 53, 0.2)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(255,255,255,0.12)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.7)';">
      <img src="/assets/certificates/badge_gcp_appdev.png" alt="Set Up an App Dev Environment on Google Cloud - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
    </div>
  </div>
</div></div></div><div class="space-150 hide-landscape">'''

html = re.sub(old_studio_grid, new_studio_grid, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated badges layout into 1 featured + 2x2 grid with interactive reactive physics!")
