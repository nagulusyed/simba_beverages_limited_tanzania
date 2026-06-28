from PIL import Image, ImageDraw
import math

def crop_to_circle():
    orig = Image.open('images/new-logo.png.jpeg').convert('RGBA')
    width, height = orig.size
    
    # Create a mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # The gear might not be perfectly touching the edges, let's say radius is slightly less than width/2
    # Let's draw a white circle on the mask
    # Bounding box for the circle: (left, top, right, bottom)
    # Looking at the map, the gear touches y=20 and y=620 roughly. So radius is about 300.
    center_x, center_y = width // 2, height // 2
    radius = 300
    
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=255)
    
    # Apply the mask
    output = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    output.paste(orig, (0, 0), mask)
    
    # Save the output
    output.save('images/sbl-logo.png')
    print("Cropped to circle perfectly.")

if __name__ == "__main__":
    crop_to_circle()
