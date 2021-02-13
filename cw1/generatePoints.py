from random import uniform
from math import cos, sin, pi


def pointsInInterval(s, t, n):
    return [(uniform(s, t), uniform(s, t)) for _ in range(n)]


def pointsInCircle(c, r, n):  # c - center, r - radius, n - number of points
    result = []
    for _ in range(n):
        fi = uniform(0, 2 * pi)
        x = c[0] + r*cos(fi)
        y = c[1] + r*sin(fi)
        result.append((x, y))
    return result


def pointsInLine(a, b, s, t, n):  # a, b - points, s,t - range, n - number of points
    def findLineParams(a, b):  # find A and B in y = Ax + B
        (x1, y1), (x2, y2) = a, b
        A = (y1 - y2) / (x1 - x2)
        B = y1 - A * x1
        return A, B

    if a[0] == b[0]:
        return [(a[0], uniform(s, t)) for _ in range(n)]

    result = []
    A, B = findLineParams(a, b)
    for _ in range(n):
        x = uniform(s, t)
        y = A * x + B
        result.append((x, y))
    return result


pointSets = [pointsInInterval(-10 ** 3, 10 ** 3, 10 ** 5),
             pointsInInterval(-10 ** 14, 10 ** 14, 10 ** 5),
             pointsInCircle((0, 0), 100, 1000),
             pointsInLine((-1., 0.,), (1., 0.1), -1000, 1000, 1000)]
