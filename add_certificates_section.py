import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the img-glitch-w block with the 4 certificate cards
old_glitch_img = r'<div class="img-glitch-w">.*?</div></div></div></section>'

new_glitch_img = '''<div class="img-glitch-w"><div class="merguez" style="max-width: 520px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.15); transition: transform 0.4s ease;"><img class="merguez-img" src="/assets/certificates/cert_google_cloud.webp" height="Auto" alt="Google Cloud Certified - Reshma Banu" parallax-img="" parallax-img-scrub="3" sizes="100vw" parallax-img-y="-8" loading="lazy" style="width: 100%; height: auto; display: block; border-radius: 12px;"/></div><div class="ballon" style="max-width: 480px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.15); transition: transform 0.4s ease;"><img class="ballon-img" src="/assets/certificates/cert_cybersecurity_intel.webp" alt="Intel Cybersecurity Certification - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="10" loading="lazy" style="width: 100%; height: auto; display: block; border-radius: 12px;"/></div><div class="cert-stack-2" style="position: absolute; bottom: 8%; left: 12%; max-width: 460px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.15); z-index: 3; transition: transform 0.4s ease;"><img src="/assets/certificates/cert_mern_stack.webp" alt="MERN Stack Certification - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="-12" loading="lazy" style="width: 100%; height: auto; display: block; border-radius: 12px;"/></div><div class="cert-stack-3" style="position: absolute; top: 12%; right: 10%; max-width: 440px; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.7); border: 1px solid rgba(255,255,255,0.15); z-index: 3; transition: transform 0.4s ease;"><img src="/assets/certificates/cert_nodejs.webp" alt="NodeJS Certification - Reshma Banu" parallax-img="" parallax-img-scrub="3" parallax-img-y="14" loading="lazy" style="width: 100%; height: auto; display: block; border-radius: 12px;"/></div></div></div></div></section>'''

html = re.sub(old_glitch_img, new_glitch_img, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added certificate images to the glitch section!")
