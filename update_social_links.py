import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero section bottom links
# Replace entire link-hero-lang-w block in hero
old_hero_lang = r'<div delay="1.5" opacity="" no-scroll="" class="link-hero-lang-w" data-reveal-init="1" style="opacity: 1;"><div class="link-hero-w"><a href="https://www.linkedin.com/company/nothin/" target="_blank" class="link hide-desk w-inline-block" style="position: relative;"><div>LKDN</div>.*?<a href="#" class="link-lang w-inline-block"><div>EN</div></a></div>'

new_hero_lang = '''<div delay="1.5" opacity="" no-scroll="" class="link-hero-lang-w" data-reveal-init="1" style="opacity: 1;"><div class="link-hero-w"><a href="https://www.linkedin.com/in/reshmabanu2328" target="_blank" class="link hide-desk w-inline-block" style="position: relative;"><div>LKDN</div><span class="link-underline" style="position: absolute; bottom: -3px; left: 0%; width: 0%; height: 1px; background: white; pointer-events: none;"></span></a><a href="https://www.linkedin.com/in/reshmabanu2328" target="_blank" class="link hide-tablet w-inline-block" style="position: relative;"><div>Linkedin</div><span class="link-underline" style="position: absolute; bottom: -3px; left: 0%; width: 0%; height: 1px; background: white; pointer-events: none;"></span></a></div><a href="#" class="link-lang w-inline-block"><div>EN</div></a></div>'''

content = re.sub(old_hero_lang, new_hero_lang, content, flags=re.DOTALL)

# 2. Update Mobile Menu links
old_menu_lang = r'<div delay="1.5" opacity="" no-scroll="" class="link-hero-lang-w"><div class="link-hero-w"><a href="https://www.linkedin.com/company/nothin/" target="_blank" class="link w-inline-block"><div>LKDN</div></a>.*?<a href="#" class="link-lang mob w-inline-block"><div>EN</div></a></div>'

new_menu_lang = '''<div delay="1.5" opacity="" no-scroll="" class="link-hero-lang-w"><div class="link-hero-w"><a href="https://www.linkedin.com/in/reshmabanu2328" target="_blank" class="link w-inline-block"><div>LKDN</div></a><a href="https://www.linkedin.com/in/reshmabanu2328" target="_blank" class="link hide-tablet w-inline-block"><div>Linkedin</div></a></div><a href="#" class="link-lang mob w-inline-block"><div>EN</div></a></div>'''

content = re.sub(old_menu_lang, new_menu_lang, content, flags=re.DOTALL)

# 3. Update Footer social links
old_footer_socials = r'<div id="w-node-_92fe2b40-7a92-f80a-554b-04fcd6a444e3-d6a444d6" class="social-links-w">.*?</div>'

new_footer_socials = '''<div id="w-node-_92fe2b40-7a92-f80a-554b-04fcd6a444e3-d6a444d6" class="social-links-w"><a opacity="" href="https://www.linkedin.com/in/reshmabanu2328" target="_blank" class="link footer w-inline-block"><div class="pointer-none">Linkedin</div></a><a opacity="" href="https://www.behance.net/nothintoshow" target="_blank" class="link footer w-inline-block"><div class="pointer-none">Behance</div></a></div>'''

content = re.sub(old_footer_socials, new_footer_socials, content, flags=re.DOTALL)

# 4. General sweep for any remaining nothin linkedin or instagram links
content = content.replace('https://www.linkedin.com/company/nothin/', 'https://www.linkedin.com/in/reshmabanu2328')
content = content.replace('https://www.instagram.com/nooothinatall/', '#')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced LinkedIn with https://www.linkedin.com/in/reshmabanu2328 and removed Instagram!")
