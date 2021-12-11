import sys
sys.path.insert(1, '../util')
from profiler import profile

b_open = ['(', '{', '[', '<']
b_close = {
    '(': ')', 
    '{': '}', 
    '[': ']', 
    '<': '>'
}

@profile
def part_one(data):
    scores = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    points = 0
    for line in data:
        expected = []
        for el in line:
            if el in b_open:
                expected.append(b_close[el])
            elif el == expected[-1]:
                expected.pop()
            else:
                points += scores[el]
                break
    return points

@profile
def part_two(data):
    lu = { ")": 1, "]": 2, "}": 3, ">": 4 }
    scores = []
    for line in data[:]:
        points = 0
        expected = []
        corrupt = False
        for el in line:
            if el in b_open:
                expected.append(b_close[el])
            elif el == expected[-1]:
                expected.pop()
            else:
                corrupt = True
                break
        if not corrupt:
            for x in reversed(expected):
                points = (5*points) + lu[x]
            scores.append(points)
    return sorted(scores)[int(len(scores)/2)]

with open("day_10_input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}") # 166191
    print(f"Part Two: {part_two(data)}") # 1152088313