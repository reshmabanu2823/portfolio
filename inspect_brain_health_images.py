import os
from PIL import Image

brain_health_dir = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\Brain_health"
files = sorted(os.listdir(brain_health_dir))

for i, f in enumerate(files):
    p = os.path.join(brain_health_dir, f)
    im = Image.open(p)
    print(f"Image {i+1} ({f}): size={im.size}, mode={im.mode}, aspect={im.size[0]/im.size[1]:.2f}")
