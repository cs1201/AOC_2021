import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import defaultdict

def get_adjacent_octopii(x,y):
    result = []
    for nx,ny in [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1)]:
        if (x,y) != (nx,ny):
            result.append((nx,ny))
    return result

@profile
def part_one(data, steps):
    flashes = 0
    for _ in range(steps):
        flashing = []
        for k in data.keys():
            data[k] += 1
            if data[k] > 9:
                flashing.append(k)

        while flashing:
            f = flashing.pop()
            if data[f] == 0:
                continue
            data[f] = 0
            flashes += 1
            for adj in get_adjacent_octopii(f[0], f[1]):
                if adj in data and data[adj] != 0:
                    data[adj] += 1
                    if data[adj] > 9:
                        flashing.append(adj)
    return flashes


@profile
def part_two(data):
    flashes = 0
    steps = 0
    while True:
        steps +=1
        flashes = 0
        flashing = []
        for k in data.keys():
            data[k] += 1
            if data[k] > 9:
                flashing.append(k)

        while flashing:
            f = flashing.pop()
            if data[f] == 0:
                continue
            data[f] = 0
            flashes += 1
            for adj in get_adjacent_octopii(f[0], f[1]):
                if adj in data and data[adj] != 0:
                    data[adj] += 1
                    if data[adj] > 9:
                        flashing.append(adj)
        if flashes == len(data):
            return steps



with open("day_11_input.txt") as f:
    data = {(x,y): int(val) for y,row in enumerate(f.readlines()) for x,val in enumerate(row.strip())}
    print(f"Part One: {part_one(data.copy(), 100)}") # 1694
    print(f"Part Two: {part_two(data.copy())}") #346