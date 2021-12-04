import sys
sys.path.insert(1, '../util')
from profiler import profile

def flipped(l):
    return list(map(list, zip(*l)))

def mark_number(board, draw):
    return [[(num, True if num == draw else marked) for num,marked in row] for row in board]

def bingo(board):
    return any(all([marked for _,marked in row]) for row in board) or \
           any(all([marked for _,marked in col]) for col in flipped(board))

def sum_unmarked(board):
    return sum(num for row in board for num,marked in row if not marked)

@profile
def play(draw, boards):
    winning_boards = []
    for num in draw:
        for i, _ in enumerate(boards):
            boards[i] = mark_number(boards[i], num)
            if bingo(boards[i]) and (i not in [x for _,x in winning_boards]):
                winning_boards.append(((sum_unmarked(boards[i]) * num),i))
    return [res for res,_ in winning_boards]

with open("day_4_input.txt") as f:
    draw = list(map(int, f.readline().strip().split(',')))
    boards = [[[(int(x), False) for x in row.split()] for row in board.split("\n")] for board in f.read().strip().split("\n\n")]
    winners = play(draw, boards)
    print(f"Part One: {winners[0]}") # 39984
    print(f"Part Two: {winners[-1]}") #  8468
