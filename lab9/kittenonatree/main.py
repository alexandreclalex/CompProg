import sys

target = int(sys.stdin.readline()[:-1])

# Adjacency list for nodes
nodes = [list() for _ in range(101)]

line = list(map(int, sys.stdin.readline().split()))
min_node = line[0]

# Populate adjacency list
while len(line) > 1:
    for i in range(1, len(line)):
        nodes[line[0]].append(line[i])
        if line[i] == min_node:
            min_node = line[0]
    line = list(map(int, sys.stdin.readline().split()))

# Dict to keep track of path down the tree
backtrace = dict()

root = min_node

def dfs(node):
    '''Depth First Search'''
    for neighbor in nodes[node]:
        if neighbor not in backtrace:
            backtrace[neighbor] = node
            dfs(neighbor)
        
dfs(min_node)

# Go through backtrace to find path down the tree
path = [target]
while path[-1] != min_node:
    path.append(backtrace[path[-1]])

print(' '.join(map(str, path)))