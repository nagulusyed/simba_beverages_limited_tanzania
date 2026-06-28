import numpy as np
from PIL import Image
import colorsys

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
print(f"Original shape: {data.shape}")

# Vectorized RGB to HSV and back is complex without cv2 or skimage.
# Let's use a simpler approach or matplotlib/skimage.
# Actually, since we know we want to replace green, we can just do a simple color distance check.
# Green in RGB is roughly (0-100, 100-255, 0-100).
# Let's iterate and convert to HSV using colorsys.
# This might be slow but image is probably not huge, let's see.

h, w, c = data.shape
for y in range(h):
    for x in range(w):
        r, g, b, a = data[y, x]
        if a > 0:
            h_val, s_val, v_val = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            # Hue for green is around 0.2 to 0.4
            if 0.15 < h_val < 0.45:
                # Change hue to brown (around 0.05 to 0.1)
                new_h = 0.08
                # Reduce saturation and value to make it look like brown glass
                new_s = max(0, s_val * 0.8)
                new_v = max(0, v_val * 0.7)
                
                new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                data[y, x, 0] = int(new_r * 255)
                data[y, x, 1] = int(new_g * 255)
                data[y, x, 2] = int(new_b * 255)

# To remove the reflection, we find the bottom of the actual bottle.
# The reflection usually has a gap of fully transparent pixels, or we can just cut off the bottom N pixels.
# The user's screenshot highlights the reflection.
# Let's look at the alpha profile from bottom up.
alpha = data[:, :, 3]
row_sums = np.sum(alpha > 0, axis=1)

# Find the lowest row that has content
bottom_row = h - 1
while bottom_row > 0 and row_sums[bottom_row] == 0:
    bottom_row -= 1

# From the bottom row, move up to find a "gap" (local minimum in width) or we can just cut the reflection.
# The reflection is connected to the bottle base. 
# The bottle base is wide, the reflection starts wide and gets narrower.
# Wait, the bottle base is straight. 
# Let's just crop the bottom 25% of the non-transparent part as a rough estimate.
# Actually, the reflection height is about equal to the distance from the bottom of the bottle to the surface.
# Let's just cut the bottom 150 pixels from the bottom-most non-transparent pixel.
# Wait, a better way: let's save the colored image first and see if we can do the crop.

new_img = Image.fromarray(data)
# Let's do a hard crop of the bottom 20% of the image bounding box.
# Find top row
top_row = 0
while top_row < h and row_sums[top_row] == 0:
    top_row += 1

bbox_height = bottom_row - top_row
# The reflection is usually the bottom 15-20% of the bounding box.
# Let's crop the bottom 15% of the bounding box.
crop_bottom = bottom_row - int(bbox_height * 0.18)

cropped_data = data[:crop_bottom, :, :]
cropped_img = Image.fromarray(cropped_data)
cropped_img.save('images/hero-bottle-brown.png')

print(f"Top row: {top_row}, Bottom row: {bottom_row}, Crop bottom: {crop_bottom}")
print("Done.")
