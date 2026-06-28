from rembg import remove
from PIL import Image

input_path = 'images/new-logo.png.jpeg'
output_path = 'images/sbl-logo.png'

print(f"Removing background from {input_path}...")
try:
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    print("Background removed successfully, saved as images/sbl-logo.png")
except Exception as e:
    print(f"Error: {e}")
