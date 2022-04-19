import sys
from collections import deque

# Store who we need erdos nums for
targets = []

# Store authors and their co-authors
authors = dict()

# Read in data
inline = sys.stdin.readline()[:-1]
while inline != '':
    tokens = inline.split(' ')
    targets.append(tokens[0])
    if tokens[0] not in authors:
        authors[tokens[0]] = set(tokens[1:])
    else:
        authors[tokens[0]].update(tokens[1:])
    
    for i in range(1, len(tokens)):
        if tokens[i] not in authors:
            authors[tokens[i]] = set()
        authors[tokens[i]].add(tokens[0])

    inline = sys.stdin.readline()[:-1]

# Initialize container for Erdos nums
erdos_nums = dict()
erdos_nums['PAUL_ERDOS'] = 0

# Initialize Queue to explore
queue = deque()
queue.append('PAUL_ERDOS')

# Iterate through queue
while len(queue) > 0:
    next_author = queue.popleft()
    next_score = erdos_nums[next_author]

    # Iterate through co-authors
    for co_author in authors[next_author]:
        # Check if we can assign a better score to the co-author
        if co_author not in erdos_nums or erdos_nums[co_author] > next_score + 1:
            erdos_nums[co_author] = next_score + 1

            # Add co-author to the queue
            queue.append(co_author)

# Iterate through targets and print their scores
for target in targets:
    sys.stdout.write(target + ' ')
    if target in erdos_nums:
        sys.stdout.write(str(erdos_nums[target]))
    else:
        sys.stdout.write('no-connection')
    sys.stdout.write('\n')

sys.stdout.flush()
