import sys

# Read in params
l, v1, v2, wait, drink = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline()[:-1])

# # If we multiply all distances by a*b, we avoid all float operations, and time is proportional to 1/(a*b)
# scale = v1*v2
# l *= scale

# Save locations of carts
carts = list(map(int, sys.stdin.readline().split()))
carts.append(l)

# Array of cost to get to any stall
costs = [-1]*(n+1)
costs[n] = 0

# Array to keep track of next
next_cart = [-1]*(n+1)

# Index of the last cart that we have solved, start at n, sice we have not solved any carts
j = n 

def cost(i, j):
    '''Returns time to go from i to j only taking coffee at i'''
    # Distance between carts
    d = carts[j] - carts[i]
    
    # How far can we get while drinking our coffee
    full_drink_d = (v1*wait + v2*drink)
    
    # We finish our coffee, and keep walking at slow speed
    if d >= full_drink_d:
        return wait + drink + (d-full_drink_d)/v1
    
    # We can start drinking it, but cannot finish it before reaching j
    elif d >= v1*wait:
        return wait + (d-v1*wait)/v2
    
    # We cannot start drinking the coffee
    return d/v1
        

# Build cost array backwards
for i in range(n-1, -1, -1):
    # Where we run out of coffee if we buy here
    run_out = carts[i] + v1*wait + v2*drink
    
    # We reach the end, no need to buy more coffee
    if run_out > l:
        costs[i] = cost(i, n)
        continue
    
    # Iterate our j back to where we know we have solved
    while j > i and carts[j] > run_out:
        j -= 1
    if i == j:
        j += 1
        
    costs[i] = cost(i, j) + costs[j]
    next_cart[i] = j

    # Try the shop after j
    if j+1 <= n and cost(i, j+1) + costs[j+1] < costs[i]:
        costs[i] = cost(i, j+1) + costs[j+1]
        next_cart[i] = j+1

res = []
if n > 0:
    res.append(0)
    j = 0
    while next_cart[j] != -1 and next_cart[j] != n:
        res.append(next_cart[j])
        j = next_cart[j]

print(len(res))
print(' '.join(map(str, res)))

