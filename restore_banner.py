from PIL import Image

def fix_banner():
    # The image with the outer background removed (but also the banner removed)
    transparent = Image.open('images/sbl-logo.png').convert("RGBA")
    
    # The original image
    orig = Image.open('images/new-logo.png.jpeg').convert("RGBA")
    
    # The banner goes from roughly y=248 to y=378
    # We will copy all pixels in this band from orig to transparent
    
    pixels_t = transparent.load()
    pixels_o = orig.load()
    
    for y in range(248, 378):
        for x in range(transparent.width):
            pixels_t[x, y] = pixels_o[x, y]
            
    transparent.save('images/sbl-logo.png')
    print("Banner restored perfectly.")

if __name__ == "__main__":
    fix_banner()
