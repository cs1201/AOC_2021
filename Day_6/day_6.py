import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import Counter

def model_lf(days, data):
    for _ in range(days):
        zeros = data.pop(0)
        data.append(zeros)
        if zeros:
            data[6] += zeros
    return sum(data)

@profile
def part_one(days, data):
    return model_lf(days, data)

@profile
def part_two(days, data): 
    return model_lf(days,data)

with open("day_6_input.txt") as f:
    c = Counter(list(map(int, f.read().split(','))))
    data = [c[i] for i in range(9)]
    print(f"Part One: {part_one(80, data[:])}") # 386536
    print(f"Part Two: {part_two(256, data[:])}") # 1732821262171