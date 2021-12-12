import sys
sys.path.insert(1, '../util')
from profiler import profile

def create_cave(data):
    cave = {}
    for v1, v2 in data:
        cave.setdefault(v1, []).append(v2)
        cave.setdefault(v2, []).append(v1)
    return cave

is_smallcave = lambda x: x.islower() and x not in ['start', 'end']

def find_paths(cave, curNode, part2=False, paths=0, curPath=[]):
    curPath.append(curNode)
    if curNode == "end":
        paths += 1
        curPath.pop()
    else:
        for child in cave[curNode]:
            if child == 'start':
                continue
            if is_smallcave(child) and child in curPath:
                if part2:
                    if any(curPath.count(x)>=2 for x in curPath if is_smallcave(x)):
                        continue
                else:
                    continue
            paths = find_paths(cave, child, part2, paths, curPath)
        curPath.pop()
    return paths
    
@profile
def part_one(data):
    return find_paths(create_cave(data), "start")

@profile
def part_two(data):
    return find_paths(create_cave(data), "start", part2=True)

with open("/Users/cston/Developer/Personal/AOC_2021/Day_12/day_12_input.txt") as f:
    data = [x.strip().split('-') for x in f.readlines()]
    print(f"Part One: {part_one(data[:])}")
    print(f"Part Two: {part_two(data[:])}")