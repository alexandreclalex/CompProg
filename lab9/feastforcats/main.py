import sys
from heapq import heappop, heappush, heapify
        
def prims(adj):
    '''Finds the mst using prim's algorithm'''
    n = len(adj)
    best = [0]*n
    remaining = set(range(1, n))
    visited = [False]*n
    visited[0] = True
    heap = []
    edges, dist = 0, 0
    for i in range(1, n):
        heappush(heap, (adj[0][i], i))
        best[i] = adj[0][i]
    while edges < n-1:
        while True:
            w, v = heappop(heap)
            if visited[v]:
                continue
            break
        edges += 1
        dist += w
        visited[v] = True
        remaining.remove(v)
        for w in remaining:
            if adj[v][w] < best[w]:
                best[w] = adj[v][w]
                heappush(heap, (adj[v][w], w))
    return best, dist
    

if __name__ =='__main__':
    num_cases = int(sys.stdin.readline()[:-1])
    for case in range(num_cases):
        milk, cats = map(int, sys.stdin.readline().split())
        
        #Create and populate adjacency list
        adj = [[0]*cats for _ in range(cats)]
        for edge in range(cats*(cats-1)//2):
            a, b, cost = map(int, sys.stdin.readline().split())
            adj[a][b] = cost
            adj[b][a] = cost
        
        # Need this much milk to feed cats
        if milk < cats*2-1:
            print('no')
        else:
            mst, dist = prims(adj)
            if dist + cats <= milk:
                print('yes')
            else:
                print('no')
        