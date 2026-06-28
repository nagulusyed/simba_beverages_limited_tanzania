import numpy as np
from PIL import Image

img = Image.open('images/hero-bottle.png').convert('RGBA')
data = np.array(img)
alpha = data[:, :, 3]

# Let's find the sum of alpha values for each row in the bottom 300 pixels
for y in range(750, 1020, 5):
    print(f"Y={y:4d}: max_alpha={np.max(alpha[y, :]):3d}, sum_alpha={np.sum(alpha[y, :]):6d}, width={np.sum(alpha[y, :] > 0)}")
