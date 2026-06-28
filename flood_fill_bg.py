from PIL import Image, ImageDraw

def remove_outer_white(input_path, output_path, threshold=200):
    print(f"Opening {input_path}")
    img = Image.open(input_path).convert("RGBA")
    
    # Get image data
    pixels = img.load()
    width, height = img.size
    
    # We will do a simple BFS/flood fill from the corners
    # to find all 'outer' white pixels and make them transparent.
    
    # Check if a pixel is 'white' (or close to it)
    def is_white(c):
        return c[0] > threshold and c[1] > threshold and c[2] > threshold
        
    visited = set()
    queue = []
    
    # Add borders to queue
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))
        
    print("Performing flood fill...")
    while queue:
        x, y = queue.pop(0)
        
        if (x, y) in visited:
            continue
            
        if x < 0 or x >= width or y < 0 or y >= height:
            continue
            
        visited.add((x, y))
        
        if is_white(pixels[x, y]):
            # Make it transparent
            pixels[x, y] = (255, 255, 255, 0)
            
            # Add neighbors to queue
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))
            
    print(f"Saving to {output_path}")
    img.save(output_path)
    print("Done!")

if __name__ == "__main__":
    remove_outer_white("images/new-logo.png.jpeg", "images/sbl-logo.png")
