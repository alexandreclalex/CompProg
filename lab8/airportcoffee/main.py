import sys

# Read in params
l, a, b, wait, drink = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline()[:-1])

# Save locations of carts
carts = list(map(int, sys.stdin.readline().split()))

# Look for the nearest cart that is ahead of the person.
def findNearestCart(current_distance):
    cart = -1
    for x in carts:
        if current_distance <= x:
            cart = x
            break
    return cart

    #Attempt to find the nearest cart
    # value = (carts[min(range(len(carts)), key=lambda i: abs(carts[i] - current_distance))])
    # index = carts.index(value)
    # if current_distance > value and index != len(carts)-1:
    #     return carts[index+1]
    # elif current_distance < value:
    #     return value
    # else:
    #     return -1

if __name__ == '__main__':
    current_distance = 0
    coffee = False
    inc = 0
    purchase = []
    cart = findNearestCart(current_distance)
    while current_distance < l:
        # Should person drink from coffee stand?
        if (current_distance + inc) >= cart:
            inc = b
            current_distance += (a * wait + b * drink)
            if cart >= 0:
                purchase.append(carts.index(cart))
            cart = findNearestCart(current_distance)
        else:
            inc = a
            current_distance += a

    print(len(purchase))
    print(' '.join(map(str, purchase)))
