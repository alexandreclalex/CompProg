from collections import deque
import sys

# Read in board to array
rows, cols = list(map(int, sys.stdin.readline()[:-1].split(' ')))
b = []
for row in range(rows):
    b.append(list(sys.stdin.readline())[:-1])

# Read in car to move, and set score to 1
x, y = list(map(int, sys.stdin.readline()[:-1].split(' ')))
x, y = x-1, y-1
b[x][y] = 1

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# Initialize open queue and iterate through
queue = deque()
queue.append((x, y))
while len(queue) > 0:
    
    # Get next place to explore
    x, y = queue.popleft()
    
    # Iterate through moves
    for dx, dy in moves:
        
        # Check if move is in bounds
        if x + dx >= 0 and x + dx < len(b) and y + dy >= 0 and y + dy < len(b[0]):
            # If we reach a Wall, we can pass
            if b[x+dx][y+dy] == '#':
                pass
            
            # If we reach a car, add 1
            elif b[x+dx][y+dy] == 'c':
                b[x+dx][y+dy] = b[x][y] + 1
                queue.append((x+dx, y+dy))
                
            # If we reach a door
            elif b[x+dx][y+dy] == 'D':
                # If the door is on the edge, we are done
                if x+dx == 0 or x+dx == len(b)-1 or y+dy == 0 or y+dy == len(b[0])-1:
                    print(b[x][y])
                    queue.clear()
                else:
                    b[x+dx][y+dy] = b[x][y]
                    queue.appendleft((x+dx, y+dy))
