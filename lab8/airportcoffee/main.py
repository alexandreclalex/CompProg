import sys

# Read in params
l, v1, v2, wait, drink = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline()[:-1])

# # If we multiply all distances by a*b, we avoid all float operations, and time is proportional to 1/(a*b)
# scale = v1*v2
# l *= scale

# Save locations of carts
carts = list(map(int, sys.stdin.readline().split()))

