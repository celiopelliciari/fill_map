from constants import *


def check_fill(pixels, x, y, new_color, width, height):
    recursions = 0
    if (0 <= x <= width-1 and 0 <= y <= height-1) and (pixels[x, y] != new_color and pixels[x, y] != WATER_BLUE and pixels[x, y] != BLACK):
        #print(x, y)
        fill_state(pixels, x, y, new_color, width, height, recursions)



def fill_state(pixels, x, y, new_color, width, height, recursions):
    recursions += 1
    #print(count)
    if recursions > 1900:
        return

    pixels[x, y] = new_color

    if (0 <= x+1 <= width-1 and 0 <= y <= height-1) and (pixels[x+1, y] != new_color and pixels[x+1, y] != WATER_BLUE and pixels[x+1, y] != BLACK):
        fill_state(pixels, x+1, y, new_color, width, height, recursions)
    if (0 <= x-1 <= width-1 and 0 <= y <= height-1) and (pixels[x-1, y] != new_color and pixels[x-1, y] != WATER_BLUE and pixels[x-1, y] != BLACK):
        fill_state(pixels, x - 1, y, new_color, width, height, recursions)
    if (0 <= x <= width-1 and 0 <= y+1 <= height-1) and (pixels[x, y+1] != new_color and pixels[x, y+1] != WATER_BLUE and pixels[x, y+1] != BLACK):
        fill_state(pixels, x, y+1, new_color, width, height, recursions)
    if (0 <= x <= width-1 and 0 <= y-1 <= height-1) and (pixels[x, y-1] != new_color and pixels[x, y-1] != WATER_BLUE and pixels[x, y-1] != BLACK):
        fill_state(pixels, x, y-1, new_color, width, height, recursions)
