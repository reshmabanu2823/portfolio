import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

# 1. Image
img_src = os.path.join(UPLOAD_DIR, 'media_1788149762788.png')
im = Image.open(img_src)
print("Uploaded image size:", im.size)

assets_dir = os.path.join(WORKSPACE, 'assets')
www_assets_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets')
os.makedirs(assets_dir, exist_ok=True)
os.makedirs(www_assets_dir, exist_ok=True)

# Save as webp and png
im.save(os.path.join(assets_dir, 'musee_bg.webp'), 'WEBP', quality=95)
im.save(os.path.join(www_assets_dir, 'musee_bg.webp'), 'WEBP', quality=95)
shutil.copyfile(img_src, os.path.join(assets_dir, 'musee_bg.png'))
shutil.copyfile(img_src, os.path.join(www_assets_dir, 'musee_bg.png'))
print("Saved musee_bg image assets!")

# 2. Video
video_src = r'C:\Users\Reshma Banu\Downloads\Generated video 1.mp4'
if os.path.exists(video_src):
    print("Found video at:", video_src, f"({os.path.getsize(video_src)/(1024*1024):.2f} MB)")
    # Copy to root and www.noth.in
    shutil.copyfile(video_src, os.path.join(WORKSPACE, 'generated_video_1.mp4'))
    shutil.copyfile(video_src, os.path.join(WORKSPACE, 'www.noth.in', 'generated_video_1.mp4'))
    print("Copied generated_video_1.mp4 to workspace successfully!")
else:
    print("Video file not found at:", video_src)
