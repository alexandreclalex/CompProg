from multiprocessing.reduction import duplicate
import sys

#Read in the Input
numstreets = int(sys.stdin.readline())
populations = list(map(int, sys.stdin.readline().split(' ')))
num_indices = int(sys.stdin.readline())
indices = []
#Parse indices into lists
for i in range(num_indices):
    indices.append(list(map(int, sys.stdin.readline().split(' '))))

#Duplicate population array, we will add the adjoining populations to this array
adj_pop = populations.copy()

#Iterate through indices and add populations
for a, b in indices:
    adj_pop[a - 1] += populations[b - 1]
    adj_pop[b - 1] += populations[a - 1]

#Find and print the street with the least population
print(adj_pop.index(min(adj_pop)) + 1)