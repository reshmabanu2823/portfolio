import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for the 5 images in .formes-w
old_formes_img_pattern = r'(<div class="formes-w">)<img src="[^"]*papier-froisse[^"]*"[^>]*><img src="[^"]*chwing[^"]*"[^>]*><img src="[^"]*bonbon[^"]*"[^>]*><img src="[^"]*asterix[^"]*"[^>]*><img src="[^"]*coeur-bulle-nb[^"]*"[^>]*>'

new_formes_imgs = r'''\1<img src="/assets/formes/blue_knot.webp" loading="eager" sizes="100vw" srcset="/assets/formes/blue_knot-p-500.webp 500w, /assets/formes/blue_knot-p-800.webp 800w, /assets/formes/blue_knot-p-1080.webp 1080w, /assets/formes/blue_knot.webp 1024w" alt="Iridescent metallic blue twisted torus knot." class="papier-form" data-formes-base-rot="0"/><img src="/assets/formes/pink_network.webp" loading="eager" sizes="100vw" srcset="/assets/formes/pink_network-p-500.webp 500w, /assets/formes/pink_network-p-800.webp 800w, /assets/formes/pink_network-p-1080.webp 1080w, /assets/formes/pink_network.webp 1024w" alt="Pink organic bubble slime network sphere." class="chewing-gum" data-formes-base-rot="0"/><img src="/assets/formes/disco_ball.webp" loading="eager" sizes="100vw" srcset="/assets/formes/disco_ball-p-500.webp 500w, /assets/formes/disco_ball-p-800.webp 800w, /assets/formes/disco_ball-p-1080.webp 1080w, /assets/formes/disco_ball.webp 1024w" alt="Mirror disco ball reflective tiled sphere." class="bonbon-copy" data-formes-base-rot="112.00026"/><img src="/assets/formes/black_puzzle.webp" loading="eager" sizes="100vw" srcset="/assets/formes/black_puzzle-p-500.webp 500w, /assets/formes/black_puzzle-p-800.webp 800w, /assets/formes/black_puzzle-p-1080.webp 1080w, /assets/formes/black_puzzle.webp 1024w" alt="Shiny black inflatable puzzle piece." class="etoile" data-formes-base-rot="0"/><img src="/assets/formes/bubble_gear.webp" loading="eager" sizes="100vw" srcset="/assets/formes/bubble_gear-p-500.webp 500w, /assets/formes/bubble_gear-p-800.webp 800w, /assets/formes/bubble_gear-p-1080.webp 1080w, /assets/formes/bubble_gear.webp 1024w" alt="Transparent bubble wrap glass gear cogwheel." class="coeur-copy" data-formes-base-rot="-18.0001"/>'''

if re.search(old_formes_img_pattern, html, flags=re.DOTALL):
    html = re.sub(old_formes_img_pattern, new_formes_imgs, html, flags=re.DOTALL)
    print("Matched and replaced using regex pattern!")
else:
    # Alternative direct replacement of individual images
    html = re.sub(r'<img src="[^"]*papier-froisse[^"]*"[^>]*>', '<img src="/assets/formes/blue_knot.webp" loading="eager" sizes="100vw" srcset="/assets/formes/blue_knot-p-500.webp 500w, /assets/formes/blue_knot-p-800.webp 800w, /assets/formes/blue_knot-p-1080.webp 1080w, /assets/formes/blue_knot.webp 1024w" alt="Iridescent metallic blue twisted torus knot." class="papier-form" data-formes-base-rot="0"/>', html)
    html = re.sub(r'<img src="[^"]*chwing[^"]*"[^>]*>', '<img src="/assets/formes/pink_network.webp" loading="eager" sizes="100vw" srcset="/assets/formes/pink_network-p-500.webp 500w, /assets/formes/pink_network-p-800.webp 800w, /assets/formes/pink_network-p-1080.webp 1080w, /assets/formes/pink_network.webp 1024w" alt="Pink organic bubble slime network sphere." class="chewing-gum" data-formes-base-rot="0"/>', html)
    html = re.sub(r'<img src="[^"]*bonbon[^"]*"[^>]*>', '<img src="/assets/formes/disco_ball.webp" loading="eager" sizes="100vw" srcset="/assets/formes/disco_ball-p-500.webp 500w, /assets/formes/disco_ball-p-800.webp 800w, /assets/formes/disco_ball-p-1080.webp 1080w, /assets/formes/disco_ball.webp 1024w" alt="Mirror disco ball reflective tiled sphere." class="bonbon-copy" data-formes-base-rot="112.00026"/>', html)
    html = re.sub(r'<img src="[^"]*asterix[^"]*"[^>]*>', '<img src="/assets/formes/black_puzzle.webp" loading="eager" sizes="100vw" srcset="/assets/formes/black_puzzle-p-500.webp 500w, /assets/formes/black_puzzle-p-800.webp 800w, /assets/formes/black_puzzle-p-1080.webp 1080w, /assets/formes/black_puzzle.webp 1024w" alt="Shiny black inflatable puzzle piece." class="etoile" data-formes-base-rot="0"/>', html)
    html = re.sub(r'<img src="[^"]*coeur-bulle-nb[^"]*"[^>]*>', '<img src="/assets/formes/bubble_gear.webp" loading="eager" sizes="100vw" srcset="/assets/formes/bubble_gear-p-500.webp 500w, /assets/formes/bubble_gear-p-800.webp 800w, /assets/formes/bubble_gear-p-1080.webp 1080w, /assets/formes/bubble_gear.webp 1024w" alt="Transparent bubble wrap glass gear cogwheel." class="coeur-copy" data-formes-base-rot="-18.0001"/>', html)
    print("Replaced individual images!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated .formes-w images with new 3D renders!")
