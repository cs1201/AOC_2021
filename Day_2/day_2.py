import sys
sys.path.insert(1, '../util')
from profiler import profile

@profile
def part_one(data):
    return sum(m for d, m in data if d == "forward") * sum(m * (1 if d == "down" else -1) for d, m in data if d == "down" or d == "up")

@profile
def part_two(data):
    x, y, a = 0, 0, 0
    for d, m in data:
        if d == "forward":
            x += m
            y += m * a
        if d == "up" or d == "down":
            a += m * (1 if d == "down" else -1)
    return x * y

with open("day_2_input.txt") as f:
    data = [(line.strip().split()[0], int(line.strip().split()[1])) for line in f.readlines()]
    print(f"Part One: {part_one(data)}") # 1654760
    print(f"Part Two: {part_two(data)}") # 1956047400

    # assert(part_one(data) == 1654760)
    # assert(part_two(data) == 1956047400)