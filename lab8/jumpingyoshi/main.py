from collections import deque
import sys

n = int(sys.stdin.readline()[:-1])

pebbles = tuple(map(int, sys.stdin.readline().split()))

graph = [[None]*n, [None]*n]
visited = [False]*n

# Keep track of nodes that can reach other nodes
# Graph[0] is move right, Graph[1] is move left
for i in range(n):
    if i+pebbles[i] < n:
        if graph[0][i+pebbles[i]] is None:
            graph[0][i+pebbles[i]] = []
        graph[0][i+pebbles[i]].append(i)
    if i-pebbles[i] >= 0:
        if graph[1][i-pebbles[i]] is None:
            graph[1][i-pebbles[i]] = []
        graph[1][i-pebbles[i]].append(i)
    
queue = deque()
queue.append(0)
visited[0] == 1

# BFS to populate visited array
while len(queue) > 0:
    node = queue.popleft()
    mid = node + pebbles[node]
    if mid < n:
        if graph[1][mid] is not None:
            for next_node in graph[1][mid]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
    mid = node - pebbles[node]
    if mid >= 0:
        if graph[0][mid] is not None:
            for next_node in graph[0][mid]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

# Find rightmost index that can be visited
for i in range(len(visited) - 1, 0, -1):
    if visited[i]:
        print(i)
        exit(0)

print(0)