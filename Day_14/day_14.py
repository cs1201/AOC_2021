import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import deque, defaultdict, Counter

def compute(start, rules, steps):
    contained_pairs = defaultdict(lambda: 0)
    contained_letters = defaultdict(lambda:0)
    for i, el in enumerate(start):
        if i < len(start)-1:
            contained_pairs[(el, start[i+1])] += 1
        contained_letters[el] += 1

    for s in range(steps):
        tmp = contained_pairs.copy()
        for pair, count in contained_pairs.items():
            if pair in rules and count > 0:
                v = rules[pair]
                tmp[pair] -= count
                tmp[(pair[0], v)] += count
                tmp[(v, pair[1])] += count
                contained_letters[v] += count
        contained_pairs = tmp.copy()
    return max(contained_letters.values()) - min(contained_letters.values())

@profile
def part_one(start, rules):
    return compute(start, rules, 10)

@profile
def part_two(start, rules):
    return compute(start, rules, 40)

with open("day_14_input.txt") as f:
    start, r_rules = f.read().split('\n\n')
    start = [x for x in start.strip()]
    rules = defaultdict(str)
    for s in r_rules.splitlines():
        pair, insert = s.split(' -> ')
        rules[tuple(pair)] = insert

    print(f"Part One: {part_one(start, rules)}") # 5656
    print(f"Part Two: {part_two(start, rules)}") # 12271437788530