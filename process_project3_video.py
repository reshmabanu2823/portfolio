import os
import shutil
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
video_src = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\WhatsApp Video 2026-08-29 at 8.05.08 PM.mp4"

if os.path.exists(video_src):
    size_mb = os.path.getsize(video_src) / (1024 * 1024)
    print(f"Video file exists! Size: {size_mb:.2f} MB")
    
    # Target video filename
    video_dst_name = "incognita_video.mp4"
    destinations = [
        os.path.join(WORKSPACE, video_dst_name),
        os.path.join(WORKSPACE, 'www.noth.in', video_dst_name),
        os.path.join(WORKSPACE, 'assets', 'work', video_dst_name),
        os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work', video_dst_name),
    ]
    
    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(video_src, dst)
        print(f"Copied to {dst}")
else:
    print(f"File not found: {video_src}")
