from collections import deque
import sys

n = int(sys.stdin.readline()[:-1])

pebbles = tuple(map(int, sys.stdin.readline().split()))
reachable = [False]*len(pebbles)

queue = deque()           

def dfs(index):
    if reachable[index]:
        return
    reachable[index] = True
    for i in range(n):
        if pebbles[index] + pebbles[i] == abs(i - index):
            queue.append(i)
            
queue.append(0)
while len(queue) > 0:
    dfs(queue.popleft())

for i in range(len(reachable) - 1, 0, -1):
    if reachable[i]:
        print(i)
        exit(0)

print(0)