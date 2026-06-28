from rembg import remove
from PIL import Image

input_path = r'C:\Users\nagul\.gemini\antigravity\brain\0f4bd387-90fd-4f66-ae99-08346d471a8b\3d_bottle_1782625263277.png'
output_path = 'images/hero-bottle.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print("Background removed successfully.")
