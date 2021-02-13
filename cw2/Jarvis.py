from generatePoints import *
from Graham import Graham

def det3x3(a, b, c):
    s1 = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    s2 = a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return s1 - s2


def divide(a, b, c):
    eps = 10 ** (-13)

    det = det3x3(a, b, c)  # computing the determinant of given interval and the point c
    if det < -eps:  # c is clockwise to the interval - it's on its right
        return -1
    elif det > eps:  # c is counterclockwise to the interval - it's on its left
        return 1
    else:  # c is within the "epsilon range" - collinear
        return 0

def findMinPoint(P, p0):
    p_min = P[0]
    for p in P:
        if divide(p0, p_min, p) < 0:
            p_min = p
        elif divide(p0, p_min, p) == 0:
            p_min = max([p, p_min], key=lambda x: intervalLength(p0, x))
    return p_min


def findp0(P):
    y_min = min(P, key=lambda point: point[1])
    smallestYs = list(filter(lambda y: y[1] <= y_min[1], P))
    return min(smallestYs, key=lambda point: point[0])

def jarvis(P):
    Pcopy = P[:]
    p0 = findp0(Pcopy)
    convex = [p0]
    p = p0
    while True:
        tmp = findMinPoint(Pcopy, p)
        if tmp != p0:
            convex.append(tmp)
        Pcopy.remove(tmp)
        p = tmp
        if p == p0:
            return convex

rectangle = [(-10, 10), (-10,-10), (10,-10), (10,10)]
pointSets = [pointsInInterval(-100, 100, 100),
                    pointsInCircle((0,0), 10, 100),
                    pointsInRectangle(rectangle, 100),
                    pointsInHalfSquareWithDiagonals(10, 10, 20, 25)]


