import sys
from collections import deque
targets = []
authors = dict()

inline = sys.stdin.readline()[:-1]
while inline != '':
    tokens = inline.split(' ')
    targets.append(tokens[0])
    tokens = set(tokens)
    for elem in tokens:
        authors[elem] = tokens
    
    inline = sys.stdin.readline()[:-1]

connections = dict()
connections['PAUL_ERDOS'] = 0
queue =deque()
queue.append('PAUL_ERDOS')
while len(queue) > 0:
    next_author = queue.popleft()
    next_score = connections[next_author]
    for connection in authors[next_author]:
        if connection not in connections or connections[connection] > next_score + 1:
            connections[connection] = next_score + 1
            queue.append(connection)
            
for target in targets:
    sys.stdout.write(target + ' ')
    if target in connections:
        sys.stdout.write(str(connections[target]))
    else:
        sys.stdout.write('no-connection')
    sys.stdout.write('\n')

sys.stdout.flush()
