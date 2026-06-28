import numpy as np
from PIL import Image

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
h, w, c = data.shape
print(f"Image shape: {h}x{w}")

# Let's find the bounding box of the non-transparent part
alpha = data[:, :, 3]
row_sums = np.sum(alpha > 0, axis=1)

top_row = 0
while top_row < h and row_sums[top_row] == 0:
    top_row += 1

bottom_row = h - 1
while bottom_row > 0 and row_sums[bottom_row] == 0:
    bottom_row -= 1

print(f"Content from Y={top_row} to Y={bottom_row}")

# Now let's find the reflection
# Usually the reflection is a mirror image. The bottom of the bottle is the widest part before it starts narrowing down in the reflection, or it has a sharp transition.
# Let's print the width of the bottle (number of non-transparent pixels) for the bottom 30% of the content.
print("Row widths for bottom part:")
for y in range(bottom_row - int((bottom_row - top_row) * 0.3), bottom_row + 1, 10):
    print(f"Y={y}: width={row_sums[y]}")

