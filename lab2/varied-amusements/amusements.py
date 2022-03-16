import sys

n, a, b, c = map(int, sys.stdin.readline().split(' '))

cache = dict()
def get_rides(depth: int, last: str) -> int:
    # Check if we have a cached result
    if (depth, last) in cache:
        return cache[(depth, last)]
    
    # Reched total number of rides to ride, return this last ride
    if depth == n:
        return 1

    total = 0

    # We just rode a, so we can now ride b or c
    if last == 'a':
        total += b * get_rides(depth + 1, 'b')
        total += c * get_rides(depth + 1, 'c')
    # We just rode b, so we can now ride a or c
    elif last == 'b':
        total += a * get_rides(depth + 1, 'a')
        total += c * get_rides(depth + 1, 'c')
    # We just rode c, so we can now ride a or b
    elif last == 'c':
        total += a * get_rides(depth + 1, 'a')
        total += b * get_rides(depth + 1, 'b')
    # We can ride all rides if this is the first move
    else:
        total += a * get_rides(depth + 1, 'a')
        total += b * get_rides(depth + 1, 'b') 
        total += c * get_rides(depth + 1, 'c')
    
    # Put result in cache
    cache[(depth, last)] = total
    return total

print(get_rides(0, '') % (10**9 + 7))


