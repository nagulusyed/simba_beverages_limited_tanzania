import numpy as np
from PIL import Image
import colorsys

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
h, w, c = data.shape

# Crop the image at Y=890 to remove the reflection
data = data[:890, :, :]
h_new = 890

# We only want to change the green background of the label to brown.
# The label is roughly between Y=550 and Y=840.
for y in range(500, 850):
    for x in range(w):
        r, g, b, a = data[y, x]
        if a > 0:
            h_val, s_val, v_val = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            # Check if the pixel is green (hue between 0.15 and 0.45, avoiding very low saturation)
            if 0.15 < h_val < 0.45 and s_val > 0.1 and v_val > 0.1:
                # Change hue to brown (approx 0.08)
                new_h = 0.08
                # Reduce saturation slightly to look like brown
                new_s = max(0, s_val * 0.9)
                new_v = max(0, v_val * 0.8)
                
                new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                data[y, x, 0] = int(new_r * 255)
                data[y, x, 1] = int(new_g * 255)
                data[y, x, 2] = int(new_b * 255)

cropped_img = Image.fromarray(data)
cropped_img.save('images/hero-bottle-final.png')
print("Image processed and saved.")
