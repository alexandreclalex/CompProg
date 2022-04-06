import sys

cache = dict()

def get_moves(board):
    moves = []
    for i in range(len(board) - 2):
        if board[i] == 'o' and board[i+1] == 'o' and board[i+2] == '-':
            moves.append((i, i+2))
    for i in range(2, len(board)):
        if board[i] == 'o' and board[i-1] == 'o' and board[i-2] == '-':
            moves.append((i, i-2))
    return moves

def play_move(board, move):
    l = list(board)
    l[move[0]] = '-'
    l[(move[0] + move[1]) // 2] = '-'
    l[move[1]] = 'o'
    return ''.join(l)

def count_stones(board):
    return len([x for x in board if x == 'o'])

def dfs(board):
    if board in cache:
        return cache[board]
    valid_moves = get_moves(board)
    if len(valid_moves) == 0:
        count = count_stones(board)
        cache[board] = count
        return count
    min_count = 12
    for move in valid_moves:
        new_board = play_move(board, move)
        count = dfs(new_board)
        cache[new_board] = count
        if count < min_count:
            min_count = count
    return min_count


num_cases = int(sys.stdin.readline())
for case in range(num_cases):
    board = sys.stdin.readline()[:-1]
    print(dfs(board))
    
    