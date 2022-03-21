import sys

cache = dict()

def numSongs(length, last = ''):
    total = 0

    #Check if we have reached end of traversal
    if length == 0:
        return 1

    #Check if we have a cached result
    if length in cache and last in cache[length]:
        return cache[length][last]

    if last == 'a':
        if length >= 2:
            total += numSongs(length - 2, 'a') #We can add 2 a's as odd + 2 = odd
            total += numSongs(length - 2, 'b') #We can add 2 b's
    elif last == 'b':
        if length >= 1:
            total += numSongs(length - 1, 'a') #We can add 1 a
        if length >= 2:
            total += numSongs(length - 2, 'b') #We can add 2 b's as even + 2 = even
    else:
        if length >= 1:
            total += numSongs(length - 1, 'a') #We can add 1 a
        if length >= 2:
            total += numSongs(length - 2, 'b') #We can ass 2 b's
    
    #If this is the first time we encounter this n, we initialize a cache entry
    if length not in cache:
        cache[length] = dict()

    #If the entry is not already in the cache, we add it to the cache
    if last is not None and last not in cache[length]:
        cache[length][last] = total
    return total
    
#Read in input
n = int(sys.stdin.readline())

#Print Result
print(numSongs(n) % (10**9 + 7))
