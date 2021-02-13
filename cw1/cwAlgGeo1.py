from generatePoints import *
import numpy as np
import random

def det2x2(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0])

def det3x3(a,b,c):
    s1 = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    s2 = a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    return s1 - s2

def det2x2withNp(a,b,c):
    auxArr = [a, b]
    arr = np.array([[v[i]-c[i] for i in range(2)] for v in auxArr])
    return np.linalg.det(arr)

def det3x3withNp(a,b,c):
    auxArr = [a,b,c]
    arr = np.array([[v[0], v[1], 1] for v in auxArr])
    return np.linalg.det(arr)

def divideWRTinterval(interval, points, eps, detFunc):
    a, b = interval
    result = [[] for _ in range(3)]  # sets for collinear, left and right WRT interval
    for c in points:
        det = detFunc(a, b, c)
        if -eps <= det <= eps:
            result[0].append(c)
        elif det > eps:
            result[1].append(c)
        else:
            result[2].append(c)

    return result


def showStats(results, epsilons, detName):
    def prepForPrinting(results, keys):
        res = []
        for key in keys:
            newTable = []
            for result in results:
                newTable.append(len(result[key]))
            res.append(newTable)
        return res

    keys = list(results[0].keys())
    tabToPrint = prepForPrinting(results, keys)

    print(detName)
    print("\t\t ", end='')  # tab for clarity
    for eps in epsilons:
        print("{:.0e}".format(eps), end=' ')
    print()
    for i, key in enumerate(keys):
        print("%8s" % key, end='')
        for res in tabToPrint[i]:
            print("%6d" % res, end='')
        print()

epsilons = [0, 1e-14, 1e-12, 1e-10]

propStats = [{"left":[None for _ in range(random.randint(0,1000))],
              "right":[None for _ in range(random.randint(0,1000))],
              "centre":[None for _ in range(random.randint(0,1000))]} for _ in range(len(epsilons))]
showStats(propStats, epsilons, "Jebacdisa")
