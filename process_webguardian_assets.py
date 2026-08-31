import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

# 1. Process image
img_src = os.path.join(UPLOAD_DIR, 'media_1788153195383.png')
im = Image.open(img_src)
print(f"Uploaded WebGuardian image size: {im.size}, mode: {im.mode}")

work_dir = os.path.join(WORKSPACE, 'assets', 'work')
www_work_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work')
os.makedirs(work_dir, exist_ok=True)
os.makedirs(www_work_dir, exist_ok=True)

# Save original PNG and WebP
shutil.copyfile(img_src, os.path.join(work_dir, 'webguardian-screenshot.png'))
shutil.copyfile(img_src, os.path.join(www_work_dir, 'webguardian-screenshot.png'))

im.save(os.path.join(work_dir, 'webguardian-screenshot.webp'), 'WEBP', quality=95)
im.save(os.path.join(www_work_dir, 'webguardian-screenshot.webp'), 'WEBP', quality=95)

# Generate responsive variants
orig_w, orig_h = im.size
aspect = orig_h / orig_w
for width in [500, 800, 1080, 1500]:
    target_w = min(width, orig_w)
    target_h = int(target_w * aspect)
    resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    fname = f'webguardian-screenshot-p-{width}.webp' if width < 1500 else 'webguardian-screenshot.webp'
    resized.save(os.path.join(work_dir, fname), 'WEBP', quality=92)
    resized.save(os.path.join(www_work_dir, fname), 'WEBP', quality=92)
    print(f"Generated {fname} ({target_w}x{target_h})")

# 2. Copy video
video_src = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\webguardian\WhatsApp Video 2026-08-29 at 8.41.42 PM.mp4"
video_dst_name = "webguardian_video.mp4"

if os.path.exists(video_src):
    print(f"Found WebGuardian video ({os.path.getsize(video_src)/(1024*1024):.2f} MB)")
    shutil.copyfile(video_src, os.path.join(WORKSPACE, video_dst_name))
    shutil.copyfile(video_src, os.path.join(WORKSPACE, 'www.noth.in', video_dst_name))
    print(f"Copied {video_dst_name} successfully!")
else:
    print("Video file not found at:", video_src)
