import os
import shutil

video_src = r"C:\Users\Reshma Banu\Videos\Screen Recordings\Screen Recording 2026-08-09 212858.mp4"
print(f"Video exists: {os.path.exists(video_src)}")
if os.path.exists(video_src):
    size_mb = os.path.getsize(video_src) / (1024 * 1024)
    print(f"Video size: {size_mb:.2f} MB")
