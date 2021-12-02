import sys
sys.path.insert(1, '../util')
from profiler import profile

@profile
def part_one(data):
    return sum(m for d, m in data if d == "forward") * sum(m for d, m in data if d == "down") - sum(m for d, m in data if d == "up")

@profile
def part_two(data):
    x, y, a = 0, 0, 0
    for d, m in data:
        if d == "forward":
            x += m
            if a:
                y += m * a
        if d == "up":
            a -= m
        if d == "down":
            a += m
    return x * y

with open("day_2_input.txt") as f:
    data = [(line.strip().split()[0], int(line.strip().split()[1])) for line in f.readlines()]
    print(f"Part One: {part_one(data)}") # 1654760
    print(f"Part Two: {part_two(data)}") # 1956047400

    # assert(part_one(data) == 1654760)
    # assert(part_two(data) == 1956047400)