import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import Counter

@profile
def model_lf(days, data):
    for _ in range(days):
        zeros = data.pop(0)
        data.append(zeros)
        if zeros:
            data[6] += zeros
    return sum(data)

with open("day_6_input.txt") as f:
    c = Counter(list(map(int, f.read().split(','))))
    data = [c[i] for i in range(9)]
    print(f"Part One: {model_lf(80, data[:])}") # 386536
    print(f"Part Two: {model_lf(256, data[:])}") # 1732821262171