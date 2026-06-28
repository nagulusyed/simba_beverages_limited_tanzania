import numpy as np
from PIL import Image
import colorsys

# Start from the full original transparent bottle
img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
h, w, c = data.shape

# 1. Color change: green to brown on the label
# The user wants the brown color to extend below the last text.
# The last text is just above the bottom glass. 
# We'll extend the Y range from 790 to 865 to cover the entire label.
for y in range(400, 865):
    for x in range(w):
        r, g, b, a = data[y, x]
        if a > 0:
            h_val, s_val, v_val = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            if 0.15 < h_val < 0.45 and s_val > 0.1 and v_val > 0.1:
                new_h = 0.08
                new_s = max(0, s_val * 0.9)
                new_v = max(0, v_val * 0.8)
                new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                data[y, x, 0] = int(new_r * 255)
                data[y, x, 1] = int(new_g * 255)
                data[y, x, 2] = int(new_b * 255)

# 2. Crop the reflection with a curved bottom.
y_check = 850
non_transparent = np.where(data[y_check, :, 3] > 0)[0]
if len(non_transparent) > 0:
    left_x = non_transparent[0]
    right_x = non_transparent[-1]
    center_x = (left_x + right_x) // 2
    bottle_width = right_x - left_x
else:
    center_x = w // 2
    bottle_width = 260

center_y = 880
rx = bottle_width / 2.0
ry = 20 # curve depth

for y in range(850, h):
    for x in range(w):
        if x < left_x or x > right_x:
            if y > center_y:
                data[y, x, 3] = 0
        else:
            val = 1.0 - ((x - center_x)**2) / (rx**2)
            if val < 0:
                val = 0
            max_y = center_y + ry * np.sqrt(val)
            if y > max_y:
                data[y, x, 3] = 0 # Make transparent

# Crop the image array to remove the empty bottom completely
crop_y = int(center_y + ry + 5)
data = data[:crop_y, :, :]

cropped_img = Image.fromarray(data)
cropped_img.save('images/hero-bottle-final3.png')
print("Image processed and saved.")
