import math


def distantaeuclid(x, y):
    return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))


def parseberlin(filename):
    net = {}
    points = []
    with open(filename, 'r') as f:
        lines = f.readlines()[6:-1]
        for line in lines:
            garbage, x, y = line.split(" ")
            points.append((float(x), float(y)))
    net['noNodes'] = len(points) - 1
    mat = [[0 for x in range(len(points) - 1)] for y in range(len(points) - 1)]
    for i in range(len(points) - 1):
        for j in range(len(points) - 1):
            if i == j:
                mat[i][j] = 0
            else:
                mat[i][j] = int(distantaeuclid(points[i], points[j]))
    net['mat'] = mat
    return net
