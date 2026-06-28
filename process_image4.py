import numpy as np
from PIL import Image
import colorsys

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
h, w, c = data.shape

# 1. Color change: green to brown only on the label
# The label is roughly between Y=400 and Y=790.
# We will leave Y > 790 alone so the bottom glass remains green.
for y in range(400, 790):
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
# Find the left and right edges of the bottle at Y=850
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

# The bottom of the bottle is usually a curve. 
# Let's say the lowest point of the bottle is at Y=900, and the edges are at Y=880.
# We can use an ellipse equation: (x - center_x)^2 / rx^2 + (y - center_y)^2 / ry^2 = 1
# y_curve = center_y + ry * sqrt(1 - (x - center_x)^2 / rx^2)
center_y = 880
rx = bottle_width / 2.0
ry = 20 # curve depth

for y in range(850, h):
    for x in range(w):
        # If x is outside the bottle width, just crop above center_y
        if x < left_x or x > right_x:
            if y > center_y:
                data[y, x, 3] = 0
        else:
            # Calculate the allowed y for this x
            val = 1.0 - ((x - center_x)**2) / (rx**2)
            if val < 0:
                val = 0
            max_y = center_y + ry * np.sqrt(val)
            if y > max_y:
                data[y, x, 3] = 0 # Make transparent

# Crop the image array to remove the empty bottom completely to save space (optional, but let's do it at max_y + 10)
crop_y = int(center_y + ry + 5)
data = data[:crop_y, :, :]

cropped_img = Image.fromarray(data)
cropped_img.save('images/hero-bottle-final2.png')
print("Image processed and saved.")
