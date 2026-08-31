import os
import shutil

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
video_src = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\webguardian\WhatsApp Video 2026-08-29 at 8.41.42 PM.mp4"

# 1. Copy video to all locations
destinations = [
    os.path.join(WORKSPACE, 'webguardian_video.mp4'),
    os.path.join(WORKSPACE, 'www.noth.in', 'webguardian_video.mp4'),
    os.path.join(WORKSPACE, 'assets', 'work', 'webguardian_video.mp4'),
    os.path.join(WORKSPACE, 'www.noth.in', 'assets', 'work', 'webguardian_video.mp4'),
]

for dst in destinations:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(video_src, dst)
    print(f"Copied video to {dst} ({os.path.getsize(dst)/(1024*1024):.2f} MB)")

# 2. Create /works/ directory with fallback pages so clicking or navigating to /works/webguardian never 404s
works_dir = os.path.join(WORKSPACE, 'works')
www_works_dir = os.path.join(WORKSPACE, 'www.noth.in', 'works')
os.makedirs(works_dir, exist_ok=True)
os.makedirs(www_works_dir, exist_ok=True)

# Create video player page for webguardian
webguardian_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WebGuardian - Clinical Dossier & Consent Engine | Reshma Banu</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #000; color: #fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 20px; }
    .back-btn { position: fixed; top: 24px; left: 24px; display: inline-flex; align-items: center; gap: 8px; color: #fff; text-decoration: none; font-size: 14px; padding: 10px 18px; border-radius: 30px; background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.15); transition: all 0.2s ease; z-index: 100; }
    .back-btn:hover { background: rgba(255,255,255,0.2); transform: translateX(-3px); }
    .video-card { width: 100%; max-width: 1100px; aspect-ratio: 16/9; border-radius: 16px; overflow: hidden; background: #111; box-shadow: 0 40px 100px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.15); margin-bottom: 24px; }
    video { width: 100%; height: 100%; object-fit: contain; background: #000; }
    h1 { font-size: 24px; font-weight: 500; margin-bottom: 6px; }
    p { color: rgba(255,255,255,0.6); font-size: 14px; }
  </style>
</head>
<body>
  <a href="/www.noth.in/index.html#works" class="back-btn">← Back to Portfolio</a>
  <div class="video-card">
    <video src="/webguardian_video.mp4" controls autoplay playsinline></video>
  </div>
  <h1>WebGuardian</h1>
  <p>Clinical Dossier & Consent Engine — Cyber Security Showcase</p>
</body>
</html>'''

for p in [os.path.join(works_dir, 'webguardian.html'), os.path.join(works_dir, 'webguardian'),
         os.path.join(www_works_dir, 'webguardian.html'), os.path.join(www_works_dir, 'webguardian')]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(webguardian_html)

# Create video player page for utopia / musicify
musicify_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lumina / Musicify | Reshma Banu</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #000; color: #fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 20px; }
    .back-btn { position: fixed; top: 24px; left: 24px; display: inline-flex; align-items: center; gap: 8px; color: #fff; text-decoration: none; font-size: 14px; padding: 10px 18px; border-radius: 30px; background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.15); transition: all 0.2s ease; z-index: 100; }
    .back-btn:hover { background: rgba(255,255,255,0.2); transform: translateX(-3px); }
    .video-card { width: 100%; max-width: 1100px; aspect-ratio: 16/9; border-radius: 16px; overflow: hidden; background: #111; box-shadow: 0 40px 100px rgba(0,0,0,0.9); border: 1px solid rgba(255,255,255,0.15); margin-bottom: 24px; }
    video { width: 100%; height: 100%; object-fit: contain; background: #000; }
    h1 { font-size: 24px; font-weight: 500; margin-bottom: 6px; }
    p { color: rgba(255,255,255,0.6); font-size: 14px; }
  </style>
</head>
<body>
  <a href="/www.noth.in/index.html#works" class="back-btn">← Back to Portfolio</a>
  <div class="video-card">
    <video src="/generated_video_1.mp4" controls autoplay playsinline></video>
  </div>
  <h1>Musicify (Lumina)</h1>
  <p>Full-Stack Music Streaming Web Application Dashboard</p>
</body>
</html>'''

for p in [os.path.join(works_dir, 'utopia.html'), os.path.join(works_dir, 'utopia'),
         os.path.join(www_works_dir, 'utopia.html'), os.path.join(www_works_dir, 'utopia')]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(musicify_html)

print("Created all fallback standalone work project video pages!")
