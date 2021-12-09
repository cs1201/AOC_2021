import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import namedtuple
from math import prod

Point = namedtuple("Point", "x y")

def get_adjacent_cells(data, x_coord, y_coord):
    result = []
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i == 0 or j == 0]:
        if 0 <= y < len(data) and 0 <= x < len(data[0]) and ((x,y) != (x_coord, y_coord)):
            result.append((data[y][x], Point(x,y)))
    return result

def find_low_points(data):
    lps = []
    for y, row in enumerate(data):
        for x, point in enumerate(row):
            adj = get_adjacent_cells(data, x,y)
            if all([x > point for x,_ in adj]):
                lps.append((point, Point(x,y)))
    return lps

def basin_size(data, lp, visited):
    val, co = lp
    points = [p for p in get_adjacent_cells(data, co.x, co.y) if val < p[0] < 9 and p not in visited]
    visited.extend(points)
    for p in points:
        basin_size(data, p, visited)
    return len(visited)

@profile
def part_one(data):
    return sum(lp+1 for lp,_ in find_low_points(data))

@profile
def part_two(data):
    return prod(sorted([basin_size(data, lp, [lp]) for lp in find_low_points(data)])[-3:])
    
with open("day_9_input.txt") as f:
    data = [[int(x) for x in line.strip()] for line in f.readlines()]
    print(f"Part One: {part_one(data)}") # 489
    print(f"Part Two: {part_two(data)}") # 1056330