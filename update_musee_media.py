import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the image
old_img = r'https://noth-in\.b-cdn\.net/freepik__photography-frontal-shot-of-a-huge-large-169-white__495122\.webp'
new_img = r'/assets/musee_bg.webp'
html = re.sub(old_img, new_img, html)

# 2. Replace the video
old_video = r'/reshma_banu_3d_typography\.mp4'
new_video = r'/generated_video_1.mp4'
html = re.sub(old_video, new_video, html)

# Check occurrences
print("musee_bg occurrences:", len(re.findall(new_img, html)))
print("generated_video_1 occurrences:", len(re.findall(new_video, html)))

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced museum background image and video!")
