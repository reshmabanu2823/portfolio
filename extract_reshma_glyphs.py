"""
Generate authentic SVG paths for letters R, E, S, H, M, A
from PPNeueMontreal-Bold font, normalized and scaled for the scattered floating cursors.
"""

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import re

font = TTFont('PPNeueMontreal-Bold.woff2')
glyph_set = font.getGlyphSet()

def get_svg_for_char(char, target_viewbox=(0, 0, 100, 100)):
    # Map character to glyph name
    cmap = font.getBestCmap()
    code = ord(char)
    glyph_name = cmap[code]
    glyph = glyph_set[glyph_name]

    pen = SVGPathPen(glyph_set)
    glyph.draw(pen)
    raw_path = pen.getCommands()

    # Get bounding box from glyph
    # Font units: head table upem = 1000
    # TTF coordinates are inverted on Y (Y goes up), SVG Y goes down
    # We need to flip Y: y -> upem - y
    return raw_path, glyph.width

print("Extracting glyphs for R, E, S, H, M, A...")
chars = ['R', 'E', 'S', 'H', 'M', 'A']
for c in chars:
    path, width = get_svg_for_char(c)
    print(f"Char {c}: width={width}, path_len={len(path)}")
