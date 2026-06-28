import numpy as np
from PIL import Image

img = Image.open('images/temp-kombu-nobg.png').convert('RGBA')
data = np.array(img)
h, w, c = data.shape
alpha = data[:, :, 3]

# Find where the reflection starts by looking at row widths in the bottom half
row_sums = np.sum(alpha > 0, axis=1)

# Find the lowest non-empty row
bottom_row = h - 1
while bottom_row > 0 and row_sums[bottom_row] == 0:
    bottom_row -= 1

# Start looking for the waist from the bottom up, or just use a fixed guess
# To be robust, let's look at the width from bottom_row - 150 to bottom_row
min_width = w
min_y = bottom_row
for y in range(bottom_row - 150, bottom_row):
    if row_sums[y] > 0 and row_sums[y] < min_width:
        min_width = row_sums[y]
        min_y = y

# min_y is the waist, i.e. the contact point with the surface.
center_y = min_y

# Find left and right edges at center_y - 20 (to get the bottle width just above the reflection)
y_check = center_y - 20
non_transparent = np.where(alpha[y_check, :] > 0)[0]
if len(non_transparent) > 0:
    left_x = non_transparent[0]
    right_x = non_transparent[-1]
    center_x = (left_x + right_x) // 2
    bottle_width = right_x - left_x
else:
    center_x = w // 2
    bottle_width = min_width

rx = bottle_width / 2.0
ry = 20 # curve depth

# Apply curve crop
for y in range(center_y - 30, h):
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
                data[y, x, 3] = 0

crop_y = int(center_y + ry + 5)
data = data[:crop_y, :, :]

cropped_img = Image.fromarray(data)
cropped_img.save('images/bottle-kombu.png')
print(f"Image cropped at waist {min_y} and saved.")
