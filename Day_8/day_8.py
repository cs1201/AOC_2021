import sys
sys.path.insert(1, '../util')
from profiler import profile

@profile
def part_one(data):
    return sum(len(x) in [2,3,4,7] for seq in data for x in seq[1])

def complete(seg):
    return not any([x == None for x in seg.values()])

def contains(a,b):
    return len(set(a) & set(b)) == len(b)

def same_elements(a,b):
    return len(a) == len(b) and set(a)&set(b) == set(a)

def num_common_segs(a, b):
    return len(set(a) & set(b))

def decode_segments(codes):
    seg = { i: None for i in range(0,10) }
    for num in codes:
        if (len(num) == 2):
            seg[1] = num
        if (len(num) == 4):
            seg[4] = num
        if (len(num) == 3):
            seg[7] = num
        if (len(num) == 7):
            seg[8] = num
    codes = [x for x in codes if x not in [seg[1], seg[4], seg[7], seg[8]]]

    while codes:
        for num in codes:
            if len(num) == 5:
                if contains(num, seg[1]):
                    seg[3] = num
                    codes.remove(num)
                    continue
                if seg[3] and seg[9] and contains(seg[9], num):
                    seg[5] = num
                    codes.remove(num)
                    continue
                if seg[3] and seg[5]:
                    seg[2] = num
                    codes.remove(num)
                    continue
            if len(num) == 6:
                if seg[9] and num_common_segs(num, seg[1]) == 2:
                    seg[0] = num
                    codes.remove(num)
                    continue
                if num_common_segs(num, seg[1]) == 1:
                    seg[6] = num
                    codes.remove(num)
                    continue
                if num_common_segs(num, seg[4]) == 4:
                    seg[9] = num
                    codes.remove(num)
                    continue            
    return {tuple(v): k for k, v in seg.items()}

@profile
def part_two(data):
    output = 0
    for entry in data:
        code, op = [[sorted(list(x)) for x in y] for y in entry]
        map = decode_segments(code)
        output += sum([map[tuple(op[i])]*(10**(3-i)) for i in range(4)])
    return output

with open("/Users/cston/Developer/Personal/AOC_2021/Day_8/day_8_input.txt") as f:
    data = [[x.split() for x in line.split('|')] for line in f.readlines() ]
    print(f"Part One: {part_one(data)}") # 321 
    print(f"Part Two: {part_two(data)}") # 1028926