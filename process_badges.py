import os
import shutil

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

cert_dir = os.path.join(WORKSPACE, 'assets', 'certificates')
www_cert_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'certificates')
os.makedirs(cert_dir, exist_ok=True)
os.makedirs(www_cert_dir, exist_ok=True)

badges = [
    ('badge_gcp_security.png', 'media_1788109605449.png'),
    ('badge_gcp_computing.png', 'media_1788109610535.png'),
    ('badge_gcp_loadbalancing.png', 'media_1788109612963.png'),
    ('badge_gcp_ml.png', 'media_1788109617913.png')
]

for out_name, src_name in badges:
    src_p = os.path.join(UPLOAD_DIR, src_name)
    shutil.copyfile(src_p, os.path.join(cert_dir, out_name))
    shutil.copyfile(src_p, os.path.join(www_cert_dir, out_name))
    print(f"Copied {out_name} -> {os.path.getsize(src_p)/1024:.1f} KB")

# Read studio section and write to a debug file
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="studio"')
end_idx = c.find('</section>', idx)
section_content = c[idx:end_idx+10]

with open('studio_section.html', 'w', encoding='utf-8') as f:
    f.write(section_content)

print(f"Extracted studio section ({len(section_content)} bytes)")
