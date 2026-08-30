import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Target .img-block-grid in #studio
old_studio_grid = r'<div id="w-node-_8c8bfc91-8576-abe0-d854-49082250bec5-78a9d1a3" class="img-block-grid">.*?</div></div></div><div class="space-150 hide-landscape">'

new_studio_grid = '''<div id="w-node-_8c8bfc91-8576-abe0-d854-49082250bec5-78a9d1a3" class="img-block-grid" style="display: grid; grid-template-columns: 1fr 1.6fr; gap: 32px; align-items: start;">
  <div parallax-scrub="1" parallax-y="-60" parallax="" id="w-node-_01baddd9-d465-59de-ee3e-5a9211c9095b-78a9d1a3" class="img-block-left" style="display: flex; flex-direction: column; align-items: flex-start;">
    <div class="img-block-left-w" style="width: 100%; max-width: 320px; border-radius: 14px; overflow: hidden; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 25px 50px rgba(0,0,0,0.75); padding: 24px; display: flex; align-items: center; justify-content: center; transition: transform 0.4s ease, box-shadow 0.4s ease;">
      <img src="/assets/certificates/badge_gcp_computing.png" alt="Google Cloud Computing Certificate - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="-8" loading="lazy" style="width: 100%; height: auto; max-height: 280px; object-fit: contain; display: block;"/>
    </div>
    <div class="space-12"></div>
    <div class="text-block-4" style="color: rgba(255,255,255,0.8); font-size: 14px; line-height: 1.4;">Google Cloud Certified<br/><span style="color: rgba(255,255,255,0.5);">Computing Foundations</span></div>
  </div>
  <div parallax-scrub="2" parallax-y="-40" parallax="" class="img-block-right-w" style="display: flex; flex-direction: column; gap: 20px; width: 100%;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; width: 100%;">
      <div style="border-radius: 12px; overflow: hidden; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 16px; display: flex; align-items: center; justify-content: center; transition: transform 0.4s ease, box-shadow 0.4s ease;">
        <img src="/assets/certificates/badge_gcp_security.png" alt="Build a Secure Google Cloud Network - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="6" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block;"/>
      </div>
      <div style="border-radius: 12px; overflow: hidden; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 16px; display: flex; align-items: center; justify-content: center; transition: transform 0.4s ease, box-shadow 0.4s ease;">
        <img src="/assets/certificates/badge_gcp_loadbalancing.png" alt="Implement Load Balancing on Compute Engine - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="10" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block;"/>
      </div>
      <div style="border-radius: 12px; overflow: hidden; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 20px 40px rgba(0,0,0,0.7); padding: 16px; display: flex; align-items: center; justify-content: center; transition: transform 0.4s ease, box-shadow 0.4s ease;">
        <img src="/assets/certificates/badge_gcp_ml.png" alt="Prepare Data for ML APIs on Google Cloud - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="14" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block;"/>
      </div>
    </div>
  </div>
</div></div></div><div class="space-150 hide-landscape">'''

html = re.sub(old_studio_grid, new_studio_grid, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added Google Cloud badges to The Studio section!")
