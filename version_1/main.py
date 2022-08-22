from PIL import Image
from functions import *
from constants import *
import sys

sys.setrecursionlimit(15000)

# Start location
x = 0
y = 0


with Image.open("world_map.bmp", "r") as infile:
    # Dimensions of infile
    height = infile.height
    width = infile.width

    # Variable to read the pixels
    pixels = infile.load()

    for y in range(height):
        for x in range(width):
            #print(x, y)
            check_fill(pixels, x, y, RED, width, height)

    infile.save('colored_world_map.bmp')
