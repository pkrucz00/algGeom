from random import uniform
from math import cos, sin, pi, sqrt

#1st set
def pointsInInterval(s, t, n):
    return [(uniform(s, t), uniform(s, t)) for _ in range(n)]

#2nd set
def pointsInCircle(c, r, n):  # c - center, r - radius, n - number of points
    result = []
    for _ in range(n):
        fi = uniform(0, 2 * pi)
        x = c[0] + r * cos(fi)
        y = c[1] + r * sin(fi)
        result.append((x, y))
    return result

#3rd set
def findLineParams(a, b):  # find A and B in y = Ax + B
    (x1, y1), (x2, y2) = a, b
    A = (y1 - y2) / (x1 - x2)
    B = y1 - A * x1
    return A, B


def intervalLength(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def makeProbabilityArray(arr):
    n = len(arr)
    lengths = [intervalLength(arr[i % n], arr[(i + 1) % n]) for i in range(n)]
    circum = sum(lengths)
    return [(arr[i % n], arr[(i + 1) % n], lengths[i] / circum) for i in range(n)]


def weightedRandomSelect(arr):  # we assume, that probabilities add to 1
    randDouble = uniform(0, 1)
    for (a, b, prob) in arr:
        randDouble -= prob
        if randDouble < 0:
            return a, b


def pointInInterval(a, b):  # a, b - points, s,t - range, n - number of points
    if a[0] == b[0]:
        s = min(a[1], b[1])
        t = max(a[1], b[1])
        return a[0], uniform(s, t)

    s, t = min(a[0], b[0]), max(a[0], b[0])
    A, B = findLineParams(a, b)

    x = uniform(s, t)
    y = A * x + B
    return x, y


def pointsInRectangle(arr, n):  # arr - array with 4 tuples representing corners of the rectangle
    probArr = makeProbabilityArray(arr)  # probArr has all the edges
    # of the rectangle in form (corner1, corner2, probability)
    result = []
    for i in range(n):
        a, b = weightedRandomSelect(probArr)  # a, b - ends of random edge
        result.append(pointInInterval(a, b))

    return result

#4th set
def pointsInHalfSquareWithDiagonals(x, y, n1, n2):  #points are only generated on the X and Y axes and on the diagonals.
    # x, y - the coordinates of the corner opposite to corner (0,0)
    #n1, n2 - number of points on axes and diagonals
    a, b, c, d = (x, 0), (0,0), (0, y), (x, y)

    arr = [(a,b, n1), (b,c, n1), #boki
           (a,c, n2), (b,d, n2)] #przekątne
    result = [a,b,c,d]
    for u, v, n in arr:
        for _ in range(n):
            result.append(pointInInterval(u,v))

    return result