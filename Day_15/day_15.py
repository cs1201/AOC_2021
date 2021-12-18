import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import defaultdict
from heapq import heapify, heappush, heappop

def get_adjacent_points(map, point, mx, my):
    x,y = point
    for nx,ny in [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1) if i == 0 or j == 0]:
        if 0 <= ny <= my and 0 <= nx <= mx and ((nx,ny) != (x, y)):
            yield (nx,ny)

def get_max_xy(map):
    return max([x for x,_ in map.keys()]), max(y for _,y in map.keys())

def shortest_path_risk(map):
    start=(0,0)
    max_x, max_y = get_max_xy(map)
    endpoint = (max_x, max_y)
    path_risks = defaultdict(lambda: None)
    path_risks[start] = 0
    adj_points = {k: get_adjacent_points(map, k, max_x, max_y) for k in map.keys()}
    q = [(0, start)]
    visited = set()
    while q:
        currisk, curpoint = heappop(q)
        if curpoint == endpoint:
            break
        if curpoint not in visited:
            visited.add(curpoint)
        for adj in adj_points[curpoint]:
            risk_to_point = currisk + map[adj]
            prev_risk = path_risks.get(adj)
            if prev_risk is None or risk_to_point < prev_risk:
                path_risks[adj] = risk_to_point
                heappush(q, (risk_to_point, adj))
    return path_risks[endpoint]

@profile
def part_one(map):
    return shortest_path_risk(map)

@profile
def part_two(map):
    new_map = map.copy()
    max_x, max_y = get_max_xy(map)
    for i in range(1,5):
        new_tile = {((x + (i * (max_x+1))), y): ((v+i-1)%9)+1 for (x,y),v in map.items()}
        new_map = {**new_map, **new_tile}
    tmp = new_map.copy()
    for i in range(1,5):
        new_row  = {(x, (y + (i * (max_y+1)))): ((v+i-1)%9)+1 for (x,y),v in tmp.items()}
        new_map = {**new_map, **new_row}
    return shortest_path_risk(new_map)

with open("day_15_input.txt") as f:
    map = {}
    for y, row in enumerate(f.readlines()):
        for x, risk in enumerate([x for x in row.strip()]):
            map[(x,y)] = int(risk)
    print(f"Part One: {part_one(map)}")
    print(f"Part Two: {part_two(map)}")