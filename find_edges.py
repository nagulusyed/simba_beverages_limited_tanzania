from PIL import Image

img = Image.open('images/new-logo.png.jpeg').convert('RGB')
pixels = img.load()

print("Left edge white segments:")
in_white = False
start = 0
for y in range(img.height):
    r,g,b = pixels[0, y]
    is_white = (r > 220 and g > 220 and b > 220)
    if is_white and not in_white:
        in_white = True
        start = y
    elif not is_white and in_white:
        in_white = False
        print(f"White from {start} to {y-1}")

if in_white:
    print(f"White from {start} to {img.height-1}")
