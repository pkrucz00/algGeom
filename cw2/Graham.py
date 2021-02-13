from generatePoints import *


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


def partition(P, start, stop, p0):
    i = start
    for j in range(start, stop):
        if divide(p0, P[stop], P[j]) < 0:
            P[i], P[j] = P[j], P[i]
            i += 1
    P[stop], P[i] = P[i], P[stop]
    return i


def quickSort(P, start, stop, p0):
    if start < stop:
        pivot = partition(P, start, stop, p0)
        quickSort(P, start, pivot - 1, p0)
        quickSort(P, pivot + 1, stop, p0)


def removeShorter(P, a, b, p0):
    if intervalLength(a, p0) < intervalLength(b, p0):
        P.remove(a)
    else:
        P.remove(b)


def removeCollinearToP0(P, p0):
    n = len(P)
    i = 0
    for _ in range(n - 1):
        if divide(p0, P[i], P[i + 1]) == 0:
            removeShorter(P, P[i], P[i + 1], p0)
        else:
            i += 1

def removeAnotherCollinear(P):
    n = len(P)
    i = 0
    for _ in range(n-2):
        tmpArr = P[i:(i+3)]
        if divide(tmpArr[0], tmpArr[1], tmpArr[2]) == 0:
            tmpArr.sort(key=lambda x: x[0])
            tmpArr.sort(key=lambda x: x[1])
            P.remove(tmpArr[1])    #deleting the middle point
        else:
            i += 1

def findp0(P):
    Arr = sorted(P, key=lambda point: point[0])
    Arr = sorted(Arr, key=lambda point: point[1])
    return Arr[0]


def Graham(P):  # P - points set
    p0 = findp0(P)

    Pcopy = P[:]  # copying the original table so we do not modify the original points set
    Pcopy.remove(p0)
    quickSort(Pcopy, 0, len(Pcopy) - 1, p0)
    removeCollinearToP0(Pcopy, p0)
    removeAnotherCollinear(Pcopy)

    stack = [p0, Pcopy[0], Pcopy[1]]

    for point in Pcopy[2:]:
        P1, P2 = stack[-2], stack[-1]
        while divide(P1, P2, point) < 0 and len(stack) > 2:
            stack.pop()
            P1, P2 = stack[-2], stack[-1]
        stack.append(point)

    return stack

arr = [(10,10), (-10, 10), (-10,-10), (10, -10)]
pointSet = pointsInRectangle(arr, 1000)





