import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Refined Studio Light Section + Dark Forms Section
studio_and_forms_replacement = '''<section id="studio" class="section info-img studio-light-section" style="position: relative; background: radial-gradient(ellipse at 50% 30%, #f7f8fa 0%, #ebedf2 55%, #dfe3e8 100%); color: #111822; overflow: hidden; padding-top: 60px; padding-bottom: 90px;">
  <!-- Smooth Top Transition from Video Hero -->
  <div class="studio-top-fade" style="position: absolute; top: 0; left: 0; right: 0; height: 160px; background: linear-gradient(180deg, #000000 0%, rgba(0,0,0,0.85) 25%, rgba(0,0,0,0.2) 65%, transparent 100%); pointer-events: none; z-index: 2;"></div>
  
  <!-- Smooth Bottom Transition to Dark Section -->
  <div class="studio-bottom-fade" style="position: absolute; bottom: 0; left: 0; right: 0; height: 160px; background: linear-gradient(0deg, #000000 0%, rgba(0,0,0,0.85) 25%, rgba(0,0,0,0.2) 65%, transparent 100%); pointer-events: none; z-index: 2;"></div>

  <div class="section-separator-blur" style="opacity: 0.15;"></div>
  <div class="container" style="position: relative; z-index: 3;">
    <div class="space-87"></div>
    <div class="info-w p-l">
      <div line="" style="color: #111822; font-weight: 500;">( The Studio )</div>
      <div line="" id="w-node-_3bffa28f-e2c9-e1ae-1640-a1877cc8ebf8-78a9d1a3" class="text-block-7" style="color: #1a202c; font-weight: 400;">We called it Reshma Banu because it started as a paradox, 
an empty space open enough to become anything: 
a campaign, a space, an event, a system...</div>
      <div class="space-24 hide-landscape"></div>
      <div class="space-24 hide-landscape"></div>
      <div class="space-24"></div>
      <div class="space-24"></div>
      
      <div id="w-node-_8c8bfc91-8576-abe0-d854-49082250bec5-78a9d1a3" class="img-block-grid" style="display: grid; grid-template-columns: 1fr 1.6fr; gap: 28px; align-items: stretch; margin-top: 24px;">
        <!-- Left Featured Shield Card -->
        <div parallax-scrub="1" parallax-y="-30" parallax="" id="w-node-_01baddd9-d465-59de-ee3e-5a9211c9095b-78a9d1a3" class="img-block-left" style="display: flex; flex-direction: column; height: 100%;">
          <div class="badge-card-hero" style="flex: 1; height: 100%; border-radius: 16px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 20px 45px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.03); padding: 24px 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; box-sizing: border-box; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-8px) scale(1.02)'; this.style.borderColor='rgba(66, 133, 244, 0.45)'; this.style.boxShadow='0 30px 60px rgba(0,0,0,0.12), 0 0 35px rgba(66, 133, 244, 0.15)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(0,0,0,0.08)'; this.style.boxShadow='0 20px 45px rgba(0,0,0,0.08)';">
            <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(66,133,244,0.03) 0%, transparent 60%); pointer-events: none;"></div>
            <img src="/assets/certificates/badge_gcp_computing.png" alt="Google Cloud Computing Certificate - Reshma Banu" loading="lazy" style="width: 100%; max-width: 160px; max-height: 160px; height: auto; object-fit: contain; display: block; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.1)); margin-bottom: 14px;"/>
            <div class="hero-card-title" style="color: #111827; font-size: 16px; font-weight: 600; letter-spacing: -0.01em; margin-bottom: 4px;">Google Cloud Certified</div>
            <div class="hero-card-subtitle" style="color: #64748b; font-size: 12px; letter-spacing: 0.02em; text-transform: uppercase; font-weight: 500;">Computing Foundations</div>
          </div>
        </div>

        <!-- Right 2x2 Skill Badges Grid -->
        <div parallax-scrub="2" parallax-y="-20" parallax="" class="img-block-right-w" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%; height: 100%;">
          <!-- Badge 1: Security -->
          <div class="badge-card-item" style="border-radius: 14px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 16px 36px rgba(0,0,0,0.07), 0 3px 10px rgba(0,0,0,0.03); padding: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(52, 168, 83, 0.45)'; this.style.boxShadow='0 28px 56px rgba(0,0,0,0.12), 0 0 25px rgba(52, 168, 83, 0.15)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(0,0,0,0.08)'; this.style.boxShadow='0 16px 36px rgba(0,0,0,0.07)';">
            <img src="/assets/certificates/badge_gcp_security.png" alt="Build a Secure Google Cloud Network - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
          </div>

          <!-- Badge 2: Load Balancing -->
          <div class="badge-card-item" style="border-radius: 14px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 16px 36px rgba(0,0,0,0.07), 0 3px 10px rgba(0,0,0,0.03); padding: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(66, 133, 244, 0.45)'; this.style.boxShadow='0 28px 56px rgba(0,0,0,0.12), 0 0 25px rgba(66, 133, 244, 0.15)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(0,0,0,0.08)'; this.style.boxShadow='0 16px 36px rgba(0,0,0,0.07)';">
            <img src="/assets/certificates/badge_gcp_loadbalancing.png" alt="Implement Load Balancing on Compute Engine - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
          </div>

          <!-- Badge 3: ML APIs -->
          <div class="badge-card-item" style="border-radius: 14px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 16px 36px rgba(0,0,0,0.07), 0 3px 10px rgba(0,0,0,0.03); padding: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(251, 188, 5, 0.45)'; this.style.boxShadow='0 28px 56px rgba(0,0,0,0.12), 0 0 25px rgba(251, 188, 5, 0.15)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(0,0,0,0.08)'; this.style.boxShadow='0 16px 36px rgba(0,0,0,0.07)';">
            <img src="/assets/certificates/badge_gcp_ml.png" alt="Prepare Data for ML APIs on Google Cloud - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
          </div>

          <!-- Badge 4: App Dev -->
          <div class="badge-card-item" style="border-radius: 14px; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 16px 36px rgba(0,0,0,0.07), 0 3px 10px rgba(0,0,0,0.03); padding: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; position: relative; overflow: hidden;" onmouseenter="this.style.transform='translateY(-6px) scale(1.03)'; this.style.borderColor='rgba(234, 67, 53, 0.45)'; this.style.boxShadow='0 28px 56px rgba(0,0,0,0.12), 0 0 25px rgba(234, 67, 53, 0.15)';" onmouseleave="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(0,0,0,0.08)'; this.style.boxShadow='0 16px 36px rgba(0,0,0,0.07)';">
            <img src="/assets/certificates/badge_gcp_appdev.png" alt="Set Up an App Dev Environment on Google Cloud - Reshma Banu" loading="lazy" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 8px;"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Forms Follow Perspective Section (Preserved on Dark Background) -->
<section class="section info-perspective" style="position: relative; background: #000000; color: #ffffff; overflow: hidden;">
  <div class="container">'''

# Search and replace the entire studio section header and contents up to the start of Forms Follow Perspective
pattern_whole = r'<section id="studio"[^>]*>.*?<div class="container">\s*<div class="space-87"></div>\s*<div class="info-w p-l">.*?</div>\s*</div>\s*</div>\s*<div class="space-150 hide-landscape">'

match = re.search(pattern_whole, html, flags=re.DOTALL)
if match:
    # Replace up to <div class="space-150 hide-landscape">
    html = html[:match.start()] + studio_and_forms_replacement + '\n    <div class="space-150 hide-landscape">' + html[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(root_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Successfully replaced and scoped studio light section!")
else:
    print("Pattern did not match, investigating...")
