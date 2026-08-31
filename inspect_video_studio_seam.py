import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Search for #studio-video styles or .section.video
video_idx = html.find('id="studio-video"')
studio_idx = html.find('id="studio"')

print("Between studio-video and studio:")
print(html[video_idx:studio_idx+300])

# Search CSS for .section.video, .musee-w, .video-w, #studio-video, .section.info-img
css_matches = re.findall(r'(\.section\.video[^{]*\{[^}]*\}|\.musee-w[^{]*\{[^}]*\}|#studio-video[^{]*\{[^}]*\})', html, flags=re.DOTALL)
print("\nCSS matches for video section:")
for c in css_matches:
    print(c)
