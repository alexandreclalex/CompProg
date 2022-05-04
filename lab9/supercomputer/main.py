import sys

# Read in params
n, k = map(int, sys.stdin.readline().split())
arr = [0] * 6


for x in range(k):
    line = (list(sys.stdin.readline().split()))
    values = list(map(int, line[1:]))
    if line[0] == 'F':
        if arr[int(values[0])-1] == 0:
            arr[int(values[0])-1] = 1
        else:
            arr[int(values[0]) - 1] = 0
    else:
        print(sum(arr[int(values[0])-1: int(values[1])]))
