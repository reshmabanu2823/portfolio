from PIL import Image
import numpy as np

im = Image.open('assets/certificates/badge_gcp_security.png')
arr = np.array(im)
print('Shape:', arr.shape)
print('Alpha min, max:', arr[:,:,3].min(), arr[:,:,3].max())
# Find where alpha > 0
non_transparent = np.where(arr[:,:,3] > 0)
print('Y range with alpha > 0:', non_transparent[0].min(), non_transparent[0].max())
print('X range with alpha > 0:', non_transparent[1].min(), non_transparent[1].max())

# Where is it not pure white background or transparent
# Is there white margin at top/bottom?
mask = (arr[:,:,3] > 0) & ~((arr[:,:,0] > 250) & (arr[:,:,1] > 250) & (arr[:,:,2] > 250))
print('Colored/content pixels Y range:', np.where(mask)[0].min(), np.where(mask)[0].max())
print('Colored/content pixels X range:', np.where(mask)[1].min(), np.where(mask)[1].max())
