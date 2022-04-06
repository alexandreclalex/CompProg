import sys

board = []
for i in range(4):
    board.extend(sys.stdin.readline()[:-1].split(' '))

B = [None, 'D', 'S', 'O']
C = [None, 'S', 'T', 'O']
D = [None, 'R', 'G', 'P']

new_board = []
for elem in board:
    new_elem = []
    new_elem.append(int(elem[0]))
    new_elem.append(B.index(elem[1]))
    new_elem.append(C.index(elem[2]))
    new_elem.append(D.index(elem[3]))
    new_board.append(new_elem)

def is_valid_set(a, b, c):
    for i in range(4):
        attr_set = set([a[i], b[i], c[i]])
        if len(attr_set) == 2:
            return False
    return True
            
found_sets = False
for i in range(len(new_board)):
    for j in range(i+1, len(new_board)):
        for k in range(j+1, len(new_board)):
            if is_valid_set(new_board[i], new_board[j], new_board[k]):
                found_sets = True
                print(str(i+1) + ' ' + str(j+1) + ' ' + str(k+1))
        
if not found_sets:
    print("no sets")