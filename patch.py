import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<div class="bottle-float">'

start_idx = content.find(start_tag)
if start_idx != -1:
    svg_start = content.find('<svg', start_idx)
    svg_end = content.find('</svg>', svg_start) + len('</svg>')
    
    new_img = '<img src="images/hero-bottle.png" alt="Vin Nkolomoka Bottle" style="height: 540px; width: auto; object-fit: contain;">'
    new_content = content[:svg_start] + new_img + content[svg_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Not found")
