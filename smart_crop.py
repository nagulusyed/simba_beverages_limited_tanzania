from PIL import Image, ImageDraw
from collections import deque

def smart_crop():
    orig = Image.open('images/new-logo.png.jpeg').convert('RGBA')
    width, height = orig.size
    
    # Create a working copy for flood fill
    work = orig.copy()
    draw = ImageDraw.Draw(work)
    
    # Draw blocking rectangles to seal the gaps on the left and right
    # The banner is roughly between y=240 and y=390.
    # The gear teeth end around x=50 to 90 on the left, and 530 to 580 on the right.
    draw.rectangle([60, 220, 110, 400], fill=(0, 0, 0, 255))
    draw.rectangle([520, 220, 580, 400], fill=(0, 0, 0, 255))
    
    pixels = work.load()
    orig_pixels = orig.load()
    
    def is_white(x, y):
        r, g, b, a = pixels[x, y]
        return r > 220 and g > 220 and b > 220
        
    visited = set()
    queue = deque()
    
    # Start flood fill from the 4 corners
    corners = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
    for c in corners:
        if is_white(*c):
            queue.append(c)
            visited.add(c)
            
    print("Performing smart flood fill...")
    while queue:
        x, y = queue.popleft()
        
        # Mark as transparent on the ORIGINAL image
        orig_pixels[x, y] = (255, 255, 255, 0)
        
        # Check neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    if is_white(nx, ny):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
    orig.save('images/sbl-logo.png')
    print("Saved perfect crop to images/sbl-logo.png")

if __name__ == "__main__":
    smart_crop()
