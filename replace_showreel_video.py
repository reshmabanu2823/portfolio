import os
import shutil
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
video_src = r"C:\Users\Reshma Banu\Downloads\Generated video 1 (1).mp4"

if os.path.exists(video_src):
    size_mb = os.path.getsize(video_src) / (1024 * 1024)
    print(f"Found source video: {size_mb:.2f} MB")
    
    # Target video filename
    target_name = "generated_video_showreel.mp4"
    destinations = [
        os.path.join(WORKSPACE, target_name),
        os.path.join(WORKSPACE, 'www.noth.in', target_name),
        os.path.join(WORKSPACE, 'assets', target_name),
        os.path.join(WORKSPACE, 'www.noth.in', 'assets', target_name)
    ]
    
    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(video_src, dst)
        print(f"Copied to {dst}")
        
    # Update HTML files
    html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
    root_html_path = os.path.join(WORKSPACE, 'index.html')
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace in showreel
    old_video_pattern = r'<video[^>]*class="showreel-light"[^>]*>.*?</video>|<video[^>]*class="showreel-light"[^>]*>'
    new_video_tag = f'<video src="/{target_name}" autoplay="true" loop="" muted="" playsinline="true" crossorigin="anonymous" class="showreel-light" style="width: 100%; height: 100%; object-fit: cover; display: block;"></video>'
    
    html = re.sub(old_video_pattern, new_video_tag, html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(root_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Successfully replaced showreel video with original quality Generated video 1 (1).mp4!")
else:
    print("Source video file not found at:", video_src)
