import sys
sys.path.insert(1, '../util')
from profiler import profile

@profile
def part_one(crabs):
    return min([sum([abs(crab-i) for crab in crabs]) for i in range(min(crabs), max(crabs))])

@profile
def part_two(crabs):
    return min([sum([int((abs(crab-i)/2)*(abs(crab-i)+1))for crab in crabs]) for i in range(min(crabs), max(crabs))])

with open("day_7_input.txt") as f:
    data = [int(x) for x in f.readline().strip().split(",")]
    print(f"Part One: {part_one(data[:])}") # 344535
    print(f"Part Two: {part_two(data[:])}") # 95581659