from PIL import Image
from queue import Queue


infile = 'spain sem suavização.tif'
outfile = 'colored spain sem suavização.tif'
WHITE = (255, 255, 255)
STARTER_COLOR = (10, 10, 10)


def main():
    with Image.open(infile, "r") as image:
        width = image.width
        height = image.height
        pixels = image.load()

        color = STARTER_COLOR
        percent = 0
        for i in range(0, width, 1):
            current_percent = round(i * 10000 / width) / 100
            if current_percent > percent + 1:
                percent += 1
                print(percent, '%')
            for j in range(0, height, 1):
                pixels, color = flood_fill(pixels, i, j, color)

        print('100 %')
        print(f'Saving image as {outfile}')
        image.save(outfile)


class Node:
    def __init__(self,
                 coordinates,
                 color: tuple = (255, 0, 0)
                 ):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.color = color

    def coordinates(self,
                    i: int = 0,
                    j: int = 0
                    ):
        return self.x + i, self.y + j


def flood_fill(pixels, i, j, color):
    if pixels[i, j] == WHITE:
        q = Queue()
        pixels[i, j] = color
        q.put(Node((i, j)))
        while not q.empty():
            n = q.get()

            if pixels[n.coordinates(0, 1)] == WHITE:
                pixels[n.coordinates(0, 1)] = color
                q.put(Node(n.coordinates(0, 1)))

            if pixels[n.coordinates(1, 0)] == WHITE:
                pixels[n.coordinates(1, 0)] = color
                q.put(Node(n.coordinates(1, 0)))

            if pixels[n.coordinates(0, -1)] == WHITE:
                pixels[n.coordinates(0, -1)] = color
                q.put(Node(n.coordinates(0, -1)))

            if pixels[n.coordinates(-1, 0)] == WHITE:
                pixels[n.coordinates(-1, 0)] = color
                q.put(Node(n.coordinates(-1, 0)))

    return pixels, iterate_color(color)


def iterate_color(color):
    r, g, b = color
    r += 20
    if r >= 255:
        r = 0
        g += 10
    if g >= 255:
        g = 0
        b += 1
    return r, g, b


if __name__ == '__main__':
    main()
