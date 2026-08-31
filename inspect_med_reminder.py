import os
from PIL import Image

med_dir = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\medicine_reminder"
if os.path.exists(med_dir):
    files = sorted(os.listdir(med_dir))
    print(f"Found {len(files)} files in medicine_reminder:")
    for f in files:
        p = os.path.join(med_dir, f)
        if os.path.isfile(p):
            im = Image.open(p)
            print(f"  {f}: size={im.size}, mode={im.mode}, aspect={im.size[0]/im.size[1]:.2f}")
else:
    print("Directory not found:", med_dir)
