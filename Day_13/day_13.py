import sys
sys.path.insert(1, '../util')
from profiler import profile
from collections import defaultdict

paper = defaultdict(lambda: '.')

def print_paper(paper):
    max_x = max([k[0] for k in paper.keys()])
    max_y = max([k[1] for k in paper.keys()])
    out='\n'
    for y in range(max_y+1):
        row=''
        for x in range(max_x+1):
            row += paper[(x,y)]
        out+=row+'\n'
    return out

def fold_paper(paper, fold):
    fold_dir, fold_pos = fold
    fold_pos = int(fold_pos)
    new_paper = paper.copy()
    for (x,y),v in paper.items():
        c = y if fold_dir == 'y' else x
        if c > fold_pos:
            new_paper.pop((x,y))
            nx = 2*fold_pos-x if fold_dir == 'x' else x
            ny = 2*fold_pos-y if fold_dir == 'y' else y
            new_paper[(nx, ny)] = '#'
    return new_paper

@profile
def part_one(paper, folds):
    return len(fold_paper(paper, folds[0]))

@profile
def part_two(paper, folds):
    for fold in folds:
        paper = fold_paper(paper, fold)
    return print_paper(paper.copy())

with open("day_13_input.txt") as f:
    dots, folds = f.read().split('\n\n')
    for dot in dots.split():
        x,y = dot.split(',')
        paper[(int(x), int(y))] = '#'
    folds = [x.strip('fold along ').split('=') for x in folds.split() if x.strip('fold along ')]
    print(f"Part One: {part_one(paper.copy(), folds)}") # 827
    print(f"Part Two: {part_two(paper.copy(), folds)}") # below:

####..##..#..#.#..#.###..####..##..###.
#....#..#.#..#.#.#..#..#.#....#..#.#..#
###..#..#.####.##...#..#.###..#....#..#
#....####.#..#.#.#..###..#....#....###.
#....#..#.#..#.#.#..#.#..#....#..#.#...
####.#..#.#..#.#..#.#..#.####..##..#...