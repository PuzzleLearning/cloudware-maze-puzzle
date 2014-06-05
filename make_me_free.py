from Queue import Queue
from PIL import Image
import sys

start = (56, 660)
end = (386, 349)
#iterations = 0
img_canvas = 0


def iswhite(value):
    if value == (255, 255, 255):
        return True


#def output(pixels):
    #global iterations
    #im = Image.new("RGB", img_canvas)
    #im.putdata(pixels)
    #im = Image.open(pixels)
    #im.save("t-" + str(iterations))


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

        #iterations += 1
        #if (iterations % 500):
        #    output(pixels)

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
    #print str(path)

    for position in path:
        x, y = position
        path_pixels[x, y] = (255, 0, 0)  # red

    #print 'iterations: ' + str(iterations)
    result_img.save(sys.argv[2])
