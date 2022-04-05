import sys

# Read in input
dims = list(map(int, sys.stdin.readline().split(' ')))

arr = []
for h in range(dims[0]):
    arr.append(list(sys.stdin.readline().replace('\n', '')))

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def propagate(i, j, arr):
    '''Propagate through land and set clouds to land'''
    for x, y in moves:
        if i + x >= 0 and i + x < len(arr) and j + y >= 0 and j + y < len(arr[0]):
            if arr[i+x][j+y] == 'C':
                arr[i+x][j+y] = 'L'
                propagate(i+x, j+y, arr)

def propagate_count(i, j, arr):
    '''Propagate through land'''
    for x, y in moves:
        if i + x >= 0 and i + x < len(arr) and j + y >= 0 and j + y < len(arr[0]):
            if arr[i+x][j+y] == 'L':
                arr[i+x][j+y] = arr[i][j]
                propagate_count(i+x, j+y, arr)

# Turn all clouds adj to land into L
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'L':
            propagate(i, j, arr)

count = 0
# Count number of islands
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'L':
            count += 1
            arr[i][j] = count
            propagate_count(i, j, arr)

print(count)