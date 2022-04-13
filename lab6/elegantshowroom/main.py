import sys

rows, cols = list(map(int, sys.stdin.readline()[:-1].split(' ')))
b = []
for row in range(rows):
    b.append(list(sys.stdin.readline())[:-1])

x, y = list(map(int, sys.stdin.readline()[:-1].split(' ')))
x, y = x-1, y-1
b[x][y] = 0

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]



def search(x, y, board):
    if board[x][y] == '#':
        return board
    for dx, dy in moves:
        print(dx, dy)
        if x + dx > 0 and x + dx < rows:
            if board[x+dx][y] == 'c':
                board[x+dx][y] = board[x][y] + 1
            elif board[x+dx][y] == 'D':
                board[x+dx][y] = board[x][y]
            elif board[x+dx][y] > board[x][y] + 1:
                board[x+dx][y] = board[x][y] + 1
            board = search(x+dx, y, board)
        if y + dy > 0 and y + dy < cols:
            if board[x][y+dy] == 'c':
                board[x][y+dy] = board[x][y] + 1
            elif board[x][y+dy] == 'D':
                board[x][y+dy] = board[x][y]
            elif board[x][y+dy] > board[x][y] + 1:
                board[x][y+dy] = board[x][y] + 1
            board = search(x, y+dy, board)
    return board

board = search(x, y, b)
print(board)