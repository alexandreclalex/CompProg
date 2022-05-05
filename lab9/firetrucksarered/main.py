import sys
from collections import deque

n = int(sys.stdin.readline()[:-1])

# Keeps track of all people with given attribute
attributes = dict()

# Keeps track of all attributes with given person
people = dict()

# Populate attributes and peoples dicts
for i in range(1, n+1):
    tokens = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tokens)):
        if tokens[j] not in attributes:
            attributes[tokens[j]] = set()
        attributes[tokens[j]].add(i)
        if i not in people:
            people[i] = set()
        people[i].add(tokens[j])

# Keep track of people that we have fully explored
linked = set([1])

# Keep track of attributes we have fully explored
exhausted_attr = set()

rules = []
queue = deque([1])

# BFS to seach for linkage between people
while len(queue) > 0:
    next_node = queue.popleft()
    for attribute in people[next_node]:
        if attribute not in exhausted_attr:
            for partner in attributes[attribute]:
                if partner not in linked:
                    linked.add(partner)
                    rules.append([next_node, partner, attribute])
                    queue.append(partner)
            exhausted_attr.add(attribute)

# We have inlinked people
if len(linked) < n:
    print('impossible')
# We have successfully linked everyone
else:
    for rule in rules:
        print(' '.join(map(str, rule)))
