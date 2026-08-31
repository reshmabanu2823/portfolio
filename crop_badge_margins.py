import os
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
cert_dir = os.path.join(WORKSPACE, 'assets', 'certificates')
www_cert_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'certificates')

skill_badges = [
    'badge_gcp_security.png',
    'badge_gcp_loadbalancing.png',
    'badge_gcp_ml.png',
    'badge_gcp_appdev.png'
]

for b in skill_badges:
    p = os.path.join(cert_dir, b)
    im = Image.open(p).convert('RGBA')
    # Crop from y=51 to y=261+1 (height=211)
    # The card rectangle is x: 0..313, y: 51..262
    cropped = im.crop((0, 51, 313, 262))
    
    # Save back to both directories
    out1 = os.path.join(cert_dir, b)
    out2 = os.path.join(www_cert_dir, b)
    cropped.save(out1, 'PNG')
    cropped.save(out2, 'PNG')
    print(f"Cropped {b}: new size = {cropped.size} (aspect ratio = {cropped.size[0]/cropped.size[1]:.2f})")

print("All skill badges cropped to full unpadded card boundaries!")
