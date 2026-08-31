from PIL import Image
import numpy as np
import os

files = [
    'badge_gcp_security.png',
    'badge_gcp_loadbalancing.png',
    'badge_gcp_ml.png',
    'badge_gcp_appdev.png'
]

for f in files:
    p = os.path.join('assets', 'certificates', f)
    im = Image.open(p).convert('RGBA')
    arr = np.array(im)
    # The badge has an outer border or colored elements
    # Let's find rows/cols that are not pure white (#ffffff) and not transparent
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    # Card content is any pixel where not (r==255 and g==255 and b==255)
    is_content = (a > 10) & ~((r > 252) & (g > 252) & (b > 252))
    rows = np.any(is_content, axis=1)
    cols = np.any(is_content, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    print(f"{f}: size={im.size}, content bounds = x:[{xmin}, {xmax}], y:[{ymin}, {ymax}], width={xmax-xmin+1}, height={ymax-ymin+1}")
    
    # Also check the card border if there is a card border outline
    # Let's check the bottom colored bar line
    # The bottom stripe is usually around ymax
    print(f"  Bottom stripe at y={ymax}")
