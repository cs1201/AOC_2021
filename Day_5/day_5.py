import sys
sys.path.insert(1, '../util')
from profiler import profile
import collections

def vent_intersections(data, consider_diagonals=False):
    points_visited = []
    for (x1,y1), (x2,y2) in data:
        if x2 < x1 or y2 < y1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x1 == x2:
            for i in range(y1, y2+1):
                points_visited.append([x1, i])
        elif y1 == y2:
            for i in range(x1, x2+1):
                points_visited.append([i, y1])
        elif consider_diagonals:
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for i in range(x2+1 - x1):
                points_visited.append([x1+i, y1+(i * (-1 if y2 < y1 else 1))])
    return len([p for p, count in collections.Counter(tuple(x) for x in points_visited).items() if count > 1])

@profile
def part_one(data):
    return vent_intersections(data)

@profile
def part_two(data):
    return vent_intersections(data, consider_diagonals=True)

with open("day_5_input.txt") as f:
    data = [[[int(co) for co in point.strip().split(",") ] for point in line.strip().split("->")] for line in f.readlines()]
    print(f"Part One: {part_one(data)}") # 4826
    print(f"Part Two: {part_two(data)}") # 16793