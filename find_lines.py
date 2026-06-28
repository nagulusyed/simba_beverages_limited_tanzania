from PIL import Image

orig = Image.open('images/new-logo.png.jpeg').convert('RGB')
pixels = orig.load()

# Find top black line
for y in range(200, 300):
    # Check middle column
    r,g,b = pixels[320, y]
    if r < 50 and g < 50 and b < 50:
        print(f"Top black line around y={y}")
        break

# Find bottom black line
for y in range(300, 450):
    r,g,b = pixels[320, y]
    if r < 50 and g < 50 and b < 50:
        print(f"Bottom black line around y={y}")
        break
