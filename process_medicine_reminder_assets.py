import os
import shutil
from PIL import Image

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
med_dir = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\medicine_reminder"

work_dir = os.path.join(WORKSPACE, 'assets', 'work')
www_work_dir = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work')
os.makedirs(work_dir, exist_ok=True)
os.makedirs(www_work_dir, exist_ok=True)

files = sorted(os.listdir(med_dir))

for i, f in enumerate(files):
    src = os.path.join(med_dir, f)
    im = Image.open(src)
    
    name_base = f"medicine_reminder_{i+1}"
    
    # Save original jpg
    shutil.copyfile(src, os.path.join(work_dir, f"{name_base}.jpg"))
    shutil.copyfile(src, os.path.join(www_work_dir, f"{name_base}.jpg"))
    
    # Save WebP
    im.save(os.path.join(work_dir, f"{name_base}.webp"), 'WEBP', quality=95)
    im.save(os.path.join(www_work_dir, f"{name_base}.webp"), 'WEBP', quality=95)
    
    # Generate responsive variants
    orig_w, orig_h = im.size
    aspect = orig_h / orig_w
    for width in [500, 800, 1080, 1600]:
        target_w = min(width, orig_w)
        target_h = int(target_w * aspect)
        resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        fname = f"{name_base}-p-{width}.webp" if width < 1600 else f"{name_base}.webp"
        resized.save(os.path.join(work_dir, fname), 'WEBP', quality=92)
        resized.save(os.path.join(www_work_dir, fname), 'WEBP', quality=92)
    
    print(f"Saved {name_base} assets ({im.size})!")

print("All Medicine Reminder image assets processed successfully!")
