import sys
sys.path.insert(1, '../util')
from profiler import profile

def flipped(l):
    return list(map(list, zip(*l)))

def check_number(board, draw):
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if board[i][j][0] == draw:
                board[i][j] = (board[i][j][0], True)
    return board

def bingo(board):
    for row in board:
        if all(x for _,x in row):
            return True
    for col in flipped(board):
        if all(x for _,x in col):
            return True
    return False

def sum_unmarked(board):
    return sum(num for row in board for num,marked in row if not marked)

@profile
def part_one(draw, boards):
    # print(draw)
    for num in draw:
        for i, board in enumerate(boards):
            boards[i] = check_number(board, num)
            if bingo(board):
                return sum_unmarked(board) * num

@profile
def part_two(draw, boards):
    winning_boards = []
    already_won = []
    for num in draw:
        for i, board in enumerate(boards):
            boards[i] = check_number(board, num)
            if bingo(board) and (i not in already_won):
                already_won.append(i)
                winning_boards.append((sum_unmarked(board) * num))
    return winning_boards[-1]

with open("day_4_input.txt") as f:
    input_f = f.readlines()
    draw = list(map(int, input_f[0].split(',')))
    boards = []
    board = []
    for line in input_f[1:]:
        if line != "\n" and line != "":
            board.append([(int(x), False) for x in line.split()])                                                
        else:
            if len(board):
                boards.append(board)
                board = []

    print(f"Part One: {part_one(draw, boards)}") # 39984
    print(f"Part Two: {part_two(draw, boards)}") #  8468