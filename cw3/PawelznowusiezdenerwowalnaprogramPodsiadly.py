import json as js


def fromJson(json_file_name):
    with open(json_file_name, 'r') as file:
        jsonList = js.loads(file.read())
    return list(map(lambda x: x['points'], [elem for elem in jsonList]))


def toJson(figures):
    with open("figures.json", 'w') as file:
        file.write(js.dumps([{"points": figure} for figure in figures]))


toJson([[(0, 7), (-1, 6), (-1, 4), (-1, 2), (0, 0), (1, 1), (1, 3), (1, 5)],
        [(5, 7), (4, 5), (3, 4), (2, 3), (3, 2), (2, 1), (6, 0)],
        [(0, 10), (-2, 8), (-1, 7.9), (-5, 5), (-1.5, 4.9), (-9, 1), (-2, 0.9), (-3, 0),
         (3, 0), (2, 0.9), (9, 1), (1.5, 4.9), (5, 5), (1, 7.9), (2, 8)]])
print(fromJson("figures.json"))
