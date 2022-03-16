import sys

cache = dict()


def numSongs(length, last = ''):
    total = 0
    if length == 0:
        return 1

    if length in cache and last in cache[length]:
        return cache[length][last]

    if last == 'a':
        if length >= 2:
            total += numSongs(length - 2, 'a')
            total += numSongs(length - 2, 'b')
    elif last == 'b':
        if length >= 1:
            total += numSongs(length - 1, 'a')
        if length >= 2:
            total += numSongs(length - 2, 'b')
    else:
        if length >= 1:
            total += numSongs(length - 1, 'a')
        if length >= 2:
            total += numSongs(length - 2, 'b')
    if length not in cache:
        cache[length] = dict()
    if last is not None and last not in cache[length]:
        cache[length][last] = total
    return total
    

n = int(sys.stdin.readline())

print(numSongs(n) % (10**9 + 7))
