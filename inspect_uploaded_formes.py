import os
from PIL import Image

uploaded_files = [
    r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189099354.png",
    r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189107329.jpg",
    r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189115452.jpg",
    r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189148184.jpg",
    r"C:\Users\Reshma Banu\.gemini\antigravity\brain\32d674cf-8476-42f9-be7e-d8b36297704a\.user_uploaded\media_1788189156916.jpg",
]

for idx, f in enumerate(uploaded_files):
    if os.path.exists(f):
        im = Image.open(f)
        print(f"Image {idx}: {os.path.basename(f)} - Size: {im.size}, Mode: {im.mode}, Format: {im.format}")
        # Check corner pixel color to see if black background
        corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
        print(f"   Corners: {corners}")
