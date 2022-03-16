import sys

#Read in the Input
numstreets = int(sys.stdin.readline())
populations = list(map(int, sys.stdin.readline().split(' ')))
num_indices = int(sys.stdin.readline())
indices = []
for i in range(num_indices):
    indices.append(list(map(int, sys.stdin.readline().split(' '))))

adj_pop = populations.copy()
for a, b in indices:
    adj_pop[a - 1] += populations[b - 1]
    adj_pop[b - 1] += populations[a - 1]

print(adj_pop.index(min(adj_pop)) + 1)