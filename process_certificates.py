import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

cert_dir = os.path.join(WORKSPACE, 'assets', 'certificates')
os.makedirs(cert_dir, exist_ok=True)

certs = [
    ('cert_cybersecurity_intel.webp', 'media_1788101554789.png'),
    ('cert_mern_stack.webp', 'media_1788101556872.png'),
    ('cert_google_cloud.webp', 'media_1788101577161.png'),
    ('cert_nodejs.webp', 'media_1788101706661.png')
]

for out_name, src_name in certs:
    src_p = os.path.join(UPLOAD_DIR, src_name)
    out_p = os.path.join(cert_dir, out_name)
    img = Image.open(src_p).convert('RGB')
    img.save(out_p, 'WEBP', quality=92)
    print(f"Saved {out_name} -> {img.size} ({os.path.getsize(out_p)/1024:.1f} KB)")

# Also copy to www.noth.in/assets/certificates
www_cert_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'certificates')
os.makedirs(www_cert_dir, exist_ok=True)
for out_name, _ in certs:
    shutil.copyfile(os.path.join(cert_dir, out_name), os.path.join(www_cert_dir, out_name))

print("Certificates processed successfully!")
