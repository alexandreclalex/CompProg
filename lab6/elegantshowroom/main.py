from collections import deque
import sys

rows, cols = list(map(int, sys.stdin.readline()[:-1].split(' ')))
b = []
for row in range(rows):
    b.append(list(sys.stdin.readline())[:-1])

x, y = list(map(int, sys.stdin.readline()[:-1].split(' ')))
x, y = x-1, y-1
b[x][y] = 1

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

queue = deque()
queue.append((x, y))
while len(queue) > 0:
    x, y = queue.popleft()
    for dx, dy in moves:
        if x + dx >= 0 and x + dx < len(b) and y + dy >= 0 and y + dy < len(b[0]):
            if b[x+dx][y+dy] == 'c':
                b[x+dx][y+dy] = b[x][y] + 1
                queue.append((x+dx, y+dy))
            elif b[x+dx][y+dy] == 'D':
                if x+dx == 0 or x+dx == len(b)-1 or y+dy == 0 or y+dy == len(b[0])-1:
                    print(b[x][y])
                    queue.clear()
                else:
                    b[x+dx][y+dy] = b[x][y]
                    queue.appendleft((x+dx, y+dy))
        