import sys

board = []
for i in range(4):
    board.append(list(map(int, sys.stdin.readline().split(' '))))

move = int(sys.stdin.readline())

def rotate(board):
    new_board = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        new_board.append(row)
        
    for i in range(4):
        for j in range(4):
            new_board[i][j] = board[j][i]
    for i in range(4):
        row = new_board[i][::-1]
        new_board[i] = row

    return new_board

def shift(board):
    for row in board:
        while 0 in row:
            row.remove(0)
        for i in range(4-len(row)):
            row.append(0)

def combine(board):
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0

for i in range(4 - move):
    board = rotate(board)

shift(board)
combine(board)
shift(board)

for i in range(move):
    board = rotate(board)

for row in board:
    print(' '.join(map(str, row)))