
def part_one(data):
    return sum([(1 if x > data[i] else 0) for i, x in enumerate(data[1:])])

def part_two(data):
    return sum([(1 if x > data[i] else 0) for i, x in enumerate(data[3:])])

with open("day_1_input.txt") as f:
    data = [x.strip() for x in f.readlines()]
    data = list(map(int, data)) # Comment out if strings needed
    print(f"Part One: {part_one(data)}") # 1167
    print(f"Part Two: {part_two(data)}") # 1130