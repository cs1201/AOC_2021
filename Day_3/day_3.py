import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import Counter

def most_common(pos):
    mc = Counter(pos).most_common(2)
    return -1 if mc[0][1] == mc[1][1] else mc[0][0]

def flipped(l):
    return list(map(list, zip(*l)))

@profile
def part_one(data): 
    g = [most_common(bit) for bit in flipped(data)]
    return int(''.join(g),2) * int(''.join(["0" if i == "1" else "1" for i in g]), 2)

@profile
def part_two(data):
    o = c = data[:]
    i = 0
    while(i < len(data)):
        if len(o) > 1:
            o = [x for x in o if x[i] == ("1" if most_common(flipped(o)[i]) in ["1", -1] else "0")]
        if len(c) > 1:
            c = [x for x in c if x[i] == ("0" if most_common(flipped(c)[i]) in ["1", -1] else "1")]
        i += 1
    return int(''.join(o[0]),2) * int(''.join(c[0]),2)

with open("day_3_input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}") # 2967914
    print(f"Part Two: {part_two(data)}") # 7041258