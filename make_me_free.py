from Queue import Queue
from PIL import Image
import sys

start = (56, 660)
end = (386, 349)
iterations = 0
img_canvas = 0


def std_write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


def iswhite(value):
    if value == (255, 255, 255):
        return True


def determineDirection(x, y, px, py):
    direction = None
    if (x > px):
        direction = 'E'
    elif (y > py):
        direction = 'S'
    elif (x < px):
        direction = 'W'
    elif (y < py):
        direction = 'N'
    else:
        direction = '-'
    return direction


def makeHerRed(pixel):
    if iswhite(pixel):
        return (225, 0, 0)
    else:
        return pixel


def drawRedLine(x, y, px, py, pixel, thick):
    black = (0, 0, 0)
    red = (225, 0, 0)  # red
    pixel[x, y] = red

    d = determineDirection(x, y, px, py)
    if (d in ['E', 'W']):
        direction = 'up'
        if pixel[x, y-1] == black:
            direction = 'down'
        if pixel[x, y+1] == black:
            direction = 'up'
        for i in range(1, thick):
            if direction == 'up':
                pixel[x, y-i] = makeHerRed(pixel[x, y-i])
            else:
                pixel[x, y+i] = makeHerRed(pixel[x, y+i])
    elif (d in ['N', 'S']):
        direction = 'left'
        if pixel[x-1, y] == black:
            direction = 'right'
        if pixel[x+1, y] == black:
            direction = 'left'
        for i in range(1, thick):
            if direction == 'left':
                pixel[x-i, y] = makeHerRed(pixel[x-i, y])
            else:
                pixel[x+i, y] = makeHerRed(pixel[x+i, y])


def getadjacent(n):
    x, y = n
    return [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]


def BFS(start, end, pixels):
    global iterations

    queue = Queue()
    queue.put([start])  # Wrapping the start tuple in a list

    while not queue.empty():

        path = queue.get()
        pixel = path[-1]

        iterations += 1
        if (iterations % 50000 == 0):
            std_write('+')

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x, y = adjacent
            if iswhite(pixels[x, y]):
                #print 'analyzing pixel x: ' + str(x) + ' and y: ' + str(y)
                pixels[x, y] = (127, 127, 127)  # see note
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    print "Queue has been exhausted. No answer was found."


if __name__ == '__main__':
    # invoke: python make_me_free.py <mazefile> <outputfile>[.jpg|.png|etc.]
    base_img = Image.open(sys.argv[1])

    gray = base_img.convert('L')
    bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
    bw.save("proper_input.png")
    print 'Transforming img to B/W, just in case..'
    base_img = Image.open("proper_input.png")
    base_img = base_img.convert('RGB')

    base_pixels = base_img.load()
    img_canvas = base_img.size
    print 'Maze is size of: ' + str(img_canvas)

    path = BFS(start, end, base_pixels)

    result_img = Image.open("proper_input.png")
    result_img = result_img.convert('RGB')
    path_pixels = result_img.load()

    px, py = path[0]
    for position in path:
        x, y = position
        drawRedLine(x, y, px, py, path_pixels, 4)
        px, py = position

    print 'Iterations processed: ' + str(iterations)
    result_img.save(sys.argv[2])
