import numpy as np
from PIL import Image
import colorsys

# Load the base hero bottle
base_img = Image.open('images/hero-bottle.png').convert('RGBA')
base_data = np.array(base_img)
h, w, c = base_data.shape

products = {
    'wine': 0.33,   # Green (Nkolo Mboka)
    'kombu': 0.08,  # Brown (Ola Kombucha)
    'ginger': 0.22, # Olive (Ginger Punch)
    'energy': 0.75  # Purple (Hard Rock)
}

for name, target_hue in products.items():
    data = base_data.copy()
    for y in range(h):
        for x in range(w):
            r, g, b, a = data[y, x]
            if a > 0:
                h_val, s_val, v_val = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
                # We want to change the green/brown parts of the bottle.
                # The hero bottle currently has green (hue ~ 0.3) and brown (hue ~ 0.08).
                # We'll shift anything with hue between 0.05 and 0.45 and moderate saturation.
                if 0.05 <= h_val <= 0.45 and s_val > 0.15:
                    new_h = target_hue
                    new_s = s_val
                    new_v = v_val
                    
                    # For purple (energy), the hue is 0.75.
                    # We might want to boost saturation slightly for energy.
                    if name == 'energy':
                        new_s = min(1.0, s_val * 1.2)
                        
                    new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                    data[y, x, 0] = int(new_r * 255)
                    data[y, x, 1] = int(new_g * 255)
                    data[y, x, 2] = int(new_b * 255)
                    
    img_out = Image.fromarray(data)
    img_out.save(f'images/bottle-{name}.png')
    print(f"Saved images/bottle-{name}.png")
