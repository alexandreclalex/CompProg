import sys
from array import *

line = sys.stdin.readline()
arr = array('b', [False]*(1000001))
while line != '':
    nums = list(map(int, line[:-1].split(' ')))
    moves = nums[2:]
    arr[0] = False
    for i in range(1, nums[0]+1):
        arr[i] = False
        for move in moves:
            if i >= move and not arr[i-move]:
                arr[i] = True
                break
    if arr[nums[0]]:
        print('Stan wins')
    else:
        print('Ollie wins')
    line = sys.stdin.readline()