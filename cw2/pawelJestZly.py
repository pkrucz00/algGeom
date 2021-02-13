from generatePoints import *
from Jarvis import jarvis


def det3x3(a,b,c):
    s1 = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    s2 = a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    return s1 - s2


def divide(a,b,c):
    eps = 10**(-13)

    det = det3x3(a, b, c)   # computing the determinant of given interval and the point c
    if det < -eps:           # c is clockwise to the interval - it's on its right
        return -1
    elif det > eps:          # c is counterclockwise to the interval - it's on its left
        return 1
    else:                    # c is within the "epsilon range" - collinear
        return 0


def removeShorter(P, i, p0):
    if intervalLength(P[i], p0) < intervalLength(P[i + 1], p0):
        del P[i]
    else:
        del P[i + 1]


def removeCollinear(P, p0):
    def removeCollinearP0(P, p0):
        n = len(P)
        i = 0
        for _ in range(n - 1):
            if divide(p0, P[i], P[i + 1]) == 0:
                removeShorter(P, i, p0)
            else:
                i += 1

    def removeCollinearSet(P):
        n = len(P)
        i = 0
        for _ in range(n - 2):
            tmpArr = P[i:(i + 3)]
            if len(tmpArr) == 3 and divide(tmpArr[0], tmpArr[1], tmpArr[2]) == 0:
                tmpArr.sort(key=lambda x: x[0])
                tmpArr.sort(key=lambda x: x[1])
                for j in range(i, i + 3):  # deleting the middle point
                    if j < len(P) and P[j] == tmpArr[1]:
                        del P[j]
            else:
                i += 1

    removeCollinearP0(P, p0)
    removeCollinearSet(P)


def partition(P, start, stop, p0):
    i = start
    for j in range(start, stop):
        if divide(p0, P[stop], P[j]) < 0:
            P[i],P[j]=P[j],P[i]
            i += 1
    P[stop],P[i] = P[i], P[stop]
    return i

def quickSort(P, start, stop, p0):
    if start < stop:
        pivot = partition(P, start, stop, p0)
        quickSort(P, start, pivot - 1, p0)
        quickSort(P, pivot + 1, stop, p0)

def findp0(P):
    y_min = min(P, key=lambda point: point[1])
    smallestYs = list(filter(lambda y: y[1] <= y_min[1], P))
    return min(smallestYs, key=lambda point: point[0])


def Graham(P):  # P - points set
    p0 = findp0(P)

    Pcopy = P[:]  # copying the original table so we do not modify the original points set
    Pcopy.remove(p0)
    quickSort(Pcopy, 0, len(Pcopy) - 1, p0)
    removeCollinear(Pcopy, p0)

    stack = [p0, Pcopy[0], Pcopy[1]]
    for point in Pcopy[2:]:
        P1, P2 = stack[-2], stack[-1]
        while divide(P1, P2, point) < 0 and len(stack) > 2:
            stack.pop()
            P1, P2 = stack[-2], stack[-1]
        stack.append(point)

    return stack



import time


def checkTime(convFunc, pointSets):
    result = []
    for pSet in pointSets:
        a = time.time()
        convFunc(pSet)
        b = time.time()
        result.append(round(b - a, 4))
    return result


timeStamps = []
numberOfPoints = list(range(1000, 3001, 1000))
functions = [Graham, jarvis]
rectangle = [(-10, 10), (-10,-10), (10,-10), (10,10)]
pointSets = [pointsInRectangle(rectangle, i) for i in numberOfPoints]

for func in functions:
    timeStamps.append(checkTime(func, pointSets))

for i in range(len(functions)):
    print(f'{functions[i].__name__}:', end='\t')
    for tStamp in timeStamps[i]:
        print(f'{tStamp}', end='\t')
    print()
