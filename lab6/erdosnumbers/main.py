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
    
    # Add target
    targets.append(tokens[0])
    tokens = set(tokens)
    
    # Add coauthors to authors dict
    for elem in tokens:
        if elem not in authors:
            authors[elem] = tokens.copy()
        else:
            authors[elem].update(tokens)
        
        # Purge self from co-authors
        authors[elem].remove(elem)
    
    inline = sys.stdin.readline()[:-1]

# Initialize container for Erdos nums
erdos_nums = dict()
erdos_nums['PAUL_ERDOS'] = 0

# Initialize Queue to explore
queue =deque()
queue.append('PAUL_ERDOS')

# Iterate through queue
while len(queue) > 0:
    next_author = queue.popleft()
    next_score = erdos_nums[next_author]
    
    # Iterate through co-authors
    for co_authors in authors[next_author]:
        # Check if we can assign a better score to the co-author
        if co_authors not in erdos_nums or erdos_nums[co_authors] > next_score + 1:
            erdos_nums[co_authors] = next_score + 1
            
            # Add co-author to the queue
            queue.append(co_authors)
            
#Iterate through targets and print their scores
for target in targets:
    sys.stdout.write(target + ' ')
    if target in erdos_nums:
        sys.stdout.write(str(erdos_nums[target]))
    else:
        sys.stdout.write('no-connection')
    sys.stdout.write('\n')

sys.stdout.flush()
