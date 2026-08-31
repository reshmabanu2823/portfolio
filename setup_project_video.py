import os
import shutil
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
video_src = r"C:\Users\Reshma Banu\Videos\Screen Recordings\Screen Recording 2026-08-09 212858.mp4"

target_dir = os.path.join(WORKSPACE, 'assets', 'work')
target_dir_www = os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work')
os.makedirs(target_dir, exist_ok=True)
os.makedirs(target_dir_www, exist_ok=True)

target_file = os.path.join(target_dir, 'screen_recording_project.mp4')
target_file_www = os.path.join(target_dir_www, 'screen_recording_project.mp4')

if os.path.exists(video_src):
    shutil.copy(video_src, target_file)
    shutil.copy(video_src, target_file_www)
    print(f"Copied video to {target_file} ({os.path.getsize(target_file)/(1024*1024):.2f} MB)")
else:
    print("Video file not found at source path!")

html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx_brain = html.find('Brain Health')
print("--- Context around Brain Health wallet ---")
print(html[idx_brain-200:idx_brain+1800])
