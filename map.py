from PIL import Image
img = Image.open('images/new-logo.png.jpeg').convert('RGB')
pixels = img.load()

for y in range(0, 640, 20):
    line = ""
    for x in range(0, 640, 10):
        r, g, b = pixels[x, y]
        if r > 220 and g > 220 and b > 220:
            line += " "
        else:
            line += "#"
    print(f"{y:3d} {line}")
