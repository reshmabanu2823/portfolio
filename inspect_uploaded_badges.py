from PIL import Image
import os

UPLOAD_DIR = r'C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded'

files = [
    'media_1788109605449.png',
    'media_1788109610535.png',
    'media_1788109612963.png',
    'media_1788109617913.png',
    'media_1788110928747.png'
]

for f in files:
    p = os.path.join(UPLOAD_DIR, f)
    im = Image.open(p)
    print(f'{f}: format={im.format}, size={im.size}, mode={im.mode}')
