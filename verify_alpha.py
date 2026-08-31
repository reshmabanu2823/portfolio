import os
from PIL import Image

formes_dir = r"C:\Users\Reshma Banu\Downloads\www.noth.in\assets\formes"

for name in ['blue_knot', 'pink_network', 'disco_ball', 'black_puzzle', 'bubble_gear']:
    path = os.path.join(formes_dir, f"{name}.png")
    im = Image.open(path)
    corner_alpha = [im.getpixel((0,0))[3], im.getpixel((im.width-1, 0))[3], im.getpixel((0, im.height-1))[3], im.getpixel((im.width-1, im.height-1))[3]]
    center_alpha = im.getpixel((im.width//2, im.height//2))[3]
    print(f"{name}: corner alpha={corner_alpha}, center alpha={center_alpha}")
