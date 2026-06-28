import numpy as np
from PIL import Image
import colorsys
from rembg import remove

# 1. Remove background
input_path = 'images/hero-bottle.png'
img = Image.open(input_path)
nobg_img = remove(img)
nobg_img = nobg_img.convert('RGBA')

data = np.array(nobg_img)
h, w, c = data.shape

# 2. Color change: label background to brown
# The original bottle's label was mostly white/grey with some greenish hues from the generation.
# We want to change the green/yellow hues to brown.
for y in range(h):
    for x in range(w):
        r, g, b, a = data[y, x]
        if a > 0:
            h_val, s_val, v_val = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            # Target green/yellow hues
            if 0.15 < h_val < 0.45 and s_val > 0.05 and v_val > 0.1:
                # But don't change the cap or neck (which are green)
                # The cap/neck is in the top 30% of the bottle
                if y > h * 0.3:
                    new_h = 0.08
                    new_s = max(0, s_val * 0.9)
                    new_v = max(0, v_val * 0.8)
                    new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                    data[y, x, 0] = int(new_r * 255)
                    data[y, x, 1] = int(new_g * 255)
                    data[y, x, 2] = int(new_b * 255)

# 3. Auto-crop to bounding box of non-transparent pixels
alpha = data[:, :, 3]
non_empty_columns = np.where(alpha.max(axis=0) > 0)[0]
non_empty_rows = np.where(alpha.max(axis=1) > 0)[0]

if len(non_empty_columns) > 0 and len(non_empty_rows) > 0:
    crop_box = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
    data = data[crop_box[0]:crop_box[1]+1, crop_box[2]:crop_box[3]+1, :]

cropped_img = Image.fromarray(data)
cropped_img.save('images/hero-bottle.png')
print("Image background removed, color matched, and auto-cropped.")
