"""
Replace the 6 scattered cursor letters (N, T, ', N, I, H) in .formes-w
with the letters R, E, S, H, M, A from PPNeueMontreal-Bold font.
"""

import re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

font = TTFont('PPNeueMontreal-Bold.woff2')
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()

# Map characters to glyphs with custom scaling and target viewBox
# The font units: cap_height ~700, upem = 1000
def create_letter_svg(char, target_w, target_h, class_name):
    code = ord(char)
    glyph_name = cmap[code]
    glyph = glyph_set[glyph_name]

    # Target height for typography in the viewBox
    # Flip Y and scale to fit target viewBox
    scale = (target_h * 0.92) / 700.0
    
    # Measure glyph bounding box approx
    pen_raw = SVGPathPen(glyph_set)
    glyph.draw(pen_raw)
    
    # We transform the glyph: scale X, scale -Y, translate to center
    tx = (target_w - glyph.width * scale) / 2.0
    ty = target_h * 0.95  # baseline near bottom

    # Create transformation matrix: [scale, 0, 0, -scale, tx, ty]
    svg_pen = SVGPathPen(glyph_set)
    tpen = TransformPen(svg_pen, (scale, 0, 0, -scale, tx, ty))
    glyph.draw(tpen)
    path_d = svg_pen.getCommands()

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {target_w} {target_h}" fill="none" class="{class_name}"><path d="{path_d}" fill="currentColor"></path></svg>'
    return svg

# The 6 letters to scatter in place of N, T, ', N, I, H:
# 1. R in place of n-cursor _2 (viewBox 0 0 62 69)
# 2. E in place of t-cursor (viewBox 0 0 31 33)
# 3. S in place of apos-cursor (viewBox 0 0 24 25)
# 4. H in place of n-cursor (viewBox 0 0 62 69)
# 5. M in place of i-cursor (viewBox 0 0 26 22)
# 6. A in place of h-cursor (viewBox 0 0 17 18)

svg_r = create_letter_svg('R', 62, 69, 'n-cursor _2')
svg_e = create_letter_svg('E', 31, 33, 't-cursor')
svg_s = create_letter_svg('S', 24, 25, 'apos-cursor')
svg_h = create_letter_svg('H', 62, 69, 'n-cursor')
svg_m = create_letter_svg('M', 22, 22, 'i-cursor')
svg_a = create_letter_svg('A', 17, 18, 'h-cursor')

scattered_block = f'''{svg_r}
{svg_h}
{svg_e}
{svg_a}
{svg_s}
{svg_m}'''

# Replace in www.noth.in/index.html and index.html
for fpath in ['www.noth.in/index.html', 'index.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern finding from first <svg.*class="n-cursor _2" to the end of last </svg> in formes-w
    pattern = r'<svg[^>]*class="n-cursor _2".*?<svg[^>]*class="i-cursor"[^>]*>.*?</svg>'
    html = re.sub(pattern, scattered_block, html, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {fpath} with scattered RESHMA letters!")

