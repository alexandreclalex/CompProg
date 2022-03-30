import sys
num_cases = int(sys.stdin.readline())
mapping = 'abcdefgh'
moves = list(zip([-1, -1, -2, -2, 1, 1, 2, 2], [2, -2, 1, -1, 2, -2, 1, -1]))
max_score = 6

def propagate(x, y, board):
    curr_score = board[x][y]
    if curr_score > max_score:
        return
    for dx, dy in moves:
        if x + dx >= 0 and x + dx < 8 and y + dy >= 0 and y + dy < 8:
            if board[x + dx][y + dy] > curr_score + 1:
                board[x + dx][y + dy] = curr_score + 1
                board = propagate(x+dx, y+dy, board)
    return board

for case in range(num_cases):
    pos = sys.stdin.readline()
    x, y = int(pos[1])-1, mapping.index(pos[0])
    board = []
    for i in range(8):
        board.append([6]*8)
    board[x][y] = 0
    board = propagate(x, y, board)
    max_val = max([max(row)for row in board])
    values = [str(max_val)]
    for i in range(7, -1, -1):
        for j in range(8):
            if board[i][j] == max_val:
                values.append(mapping[j] + str(i + 1))
    print(' '.join(values))
    