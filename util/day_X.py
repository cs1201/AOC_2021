
def part_one(data):
    ...

def part_two(data):
    ...

with open("day_X_input.txt") as f:
    data = [x.strip() for x in f.readlines()]
    data = list(map(int, data)) # Comment out if strings needed
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")