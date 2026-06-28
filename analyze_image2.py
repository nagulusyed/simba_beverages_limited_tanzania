import numpy as np
from PIL import Image

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
alpha = data[:, :, 3]
row_sums = np.sum(alpha > 0, axis=1)

print("Row widths for Y=850 to 900:")
for y in range(850, 900, 2):
    print(f"Y={y}: width={row_sums[y]}")
