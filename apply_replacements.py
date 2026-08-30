import re
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# 1. Load Font
font_path = os.path.join(WORKSPACE, 'PPNeueMontreal-Bold.woff2')
font = TTFont(font_path)
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()

def get_glyph_data(char):
    g_id = cmap.get(ord(char))
    glyph = glyph_set[g_id]
    bp = BoundsPen(glyph_set)
    glyph.draw(bp)
    xmin, ymin, xmax, ymax = bp.bounds
    return glyph, xmin, ymin, xmax, ymax, glyph.width

# 2. Build Loader R Path
glyph, xmin, ymin, xmax, ymax, advance = get_glyph_data('R')
target_h = 120.0
cap_h = 715.0
scale = target_h / cap_h
svg_pen = SVGPathPen(glyph_set)
t_pen = TransformPen(svg_pen, (scale, 0, 0, -scale, -xmin * scale, target_h))
glyph.draw(t_pen)
loader_r_d = svg_pen.getCommands()
loader_r_w = round((xmax - xmin) * scale, 1)

new_loader_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {loader_r_w} 120" fill="none" class="n-load"><path d="{loader_r_d}" fill="currentColor"></path></svg>'

# 3. Build RESHMA BANU Paths (Hero, Footer, Nav)
target_h = 280.0
scale = target_h / cap_h
space_w = 60.0
letter_gap = 14.0

cur_x = 0.0
hero_paths_list = []
text = 'RESHMA BANU'
letter_classes = ['nav-r-first', 'nav-e', 'nav-s', 'nav-h', 'nav-m', 'nav-a1', 'nav-b', 'nav-a2', 'nav-n', 'nav-u']

letter_idx = 0
for c in text:
    if c == ' ':
        cur_x += space_w
        continue
    glyph, xmin, ymin, xmax, ymax, advance = get_glyph_data(c)
    svg_pen = SVGPathPen(glyph_set)
    t_pen = TransformPen(svg_pen, (scale, 0, 0, -scale, cur_x - xmin * scale, 7.0 + target_h))
    glyph.draw(t_pen)
    w = (xmax - xmin) * scale
    c_name = letter_classes[letter_idx]
    hero_paths_list.append((c, c_name, cur_x, w, svg_pen.getCommands()))
    cur_x += w + letter_gap
    letter_idx += 1

total_w = round(cur_x - letter_gap, 1)
print(f'Total Hero / Nav Width: {total_w}')

hero_paths_html = ''.join([f'<path d="{p[4]}" fill="currentColor"></path>' for p in hero_paths_list])
new_hero_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {total_w} 294" fill="none" class="nothin-hero-svg">{hero_paths_html}</svg>'
new_footer_svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {total_w} 294" fill="none" class="footer-nothin-svg">{hero_paths_html}</svg>'

nav_paths_html = ''.join([f'<path d="{p[4]}" fill="currentColor" class="{p[1]}"></path>' for p in hero_paths_list])
new_nav_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 291" fill="none" class="nav-logo">{nav_paths_html}</svg>'

# 4. Update www.noth.in/index.html
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Loader SVG
content = re.sub(r'<svg[^>]*class="n-load"[^>]*>.*?</svg>', new_loader_svg, content, flags=re.DOTALL)

# Replace Hero SVG
content = re.sub(r'<svg[^>]*class="nothin-hero-svg"[^>]*>.*?</svg>', new_hero_svg, content, flags=re.DOTALL)

# Replace Footer SVG
content = re.sub(r'<svg[^>]*class="footer-nothin-svg"[^>]*>.*?</svg>', new_footer_svg, content, flags=re.DOTALL)

# Replace Nav Logo SVG
content = re.sub(r'<svg[^>]*class="nav-logo"[^>]*>.*?</svg>', new_nav_svg, content, flags=re.DOTALL)

# Update Title and Meta tags
content = content.replace("<title>Nothin&#x27; | Home</title>", "<title>Reshma Banu | Home</title>")
content = content.replace('content="Nothin&#x27; | Home"', 'content="Reshma Banu | Home"')
content = content.replace("Nothin&#x27; A protean augmented-creative", "Reshma Banu A protean augmented-creative")
content = content.replace('"name": "Nothin\'"', '"name": "Reshma Banu"')

# Update text content
content = content.replace('Because Nothin’ is Everythin’.', 'Because Reshma Banu is Everythin’.')
content = content.replace('Because Nothin\' is Everythin\'.', 'Because Reshma Banu is Everythin\'.')
content = content.replace('We called it Nothin’', 'We called it Reshma Banu')
content = content.replace('We called it Nothin\'', 'We called it Reshma Banu')
content = content.replace('Nothin’ without people :', 'Reshma Banu without people :')
content = content.replace('Nothin\' without people :', 'Reshma Banu without people :')
content = content.replace('we are nothin’', 'we are reshma banu')
content = content.replace('we are nothin\'', 'we are reshma banu')
content = content.replace('from nothin’', 'from reshma banu')
content = content.replace('from nothin\'', 'from reshma banu')

# Ensure local main.js is loaded
content = content.replace("https://nothinv1.netlify.app/main.js", "/nothinv1.netlify.app/main.js")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated www.noth.in/index.html successfully!")

# 5. Update nothinv1.netlify.app/main.js
js_path = os.path.join(WORKSPACE, 'nothinv1.netlify.app', 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Update Mv function for nav logo hover animation
# Replace nav letter classes array and widths
old_mv_pattern = r'function Mv\(\)\{.*?const v=!!document\.querySelector\("\.nothin-hero-svg"\);'
# Let's inspect or replace the Mv function specifically
js_content = js_content.replace(
    'n=["nav-o","nav-t","nav-h","nav-i","nav-n-last"]',
    'n=["nav-e","nav-s","nav-h","nav-m","nav-a1","nav-b","nav-a2","nav-n","nav-u"]'
)
js_content = js_content.replace(
    'const s=-1060,o=338,a=1398,c=320,l={w:o},u={x:s};',
    f'const s=0,o=250,a={total_w},c=320,l={{w:o}},u={{x:s}};'
)
js_content = js_content.replace('m([0,1,2,3,4])', 'm([0,1,2,3,4,5,6,7,8])')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated nothinv1.netlify.app/main.js successfully!")
