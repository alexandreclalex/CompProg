import sys


def bin_search_l(arr, target):
    '''Run Binary Search, erring on left side'''
    minimum, maximum = 0, len(arr) - 1
    while maximum - minimum > 1:
        middle = (minimum + maximum)//2
        if arr[middle] < target:
            minimum = middle
        else:
            maximum = middle
    if arr[minimum] < target:
        return minimum + 1
    return minimum

def bin_search_r(arr, target):
    '''Run Binary Search, erring on right side'''
    minimum, maximum = 0, len(arr) - 1
    while maximum - minimum > 1:
        middle = (minimum + maximum)//2
        if arr[middle] <= target:
            minimum = middle
        else:
            maximum = middle
    if arr[maximum] > target:
        return maximum - 1
    return maximum

# Read input and sort cards
num_cards = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split(' ')))
cards = sorted(cards)
num_ranges = int(sys.stdin.readline())

# Iterate through the ranges
for i in range(num_ranges):
    # Read in range
    lo, hi = map(int, sys.stdin.readline().split(' '))
    
    # Check if in bounds
    if cards[0] > hi or cards[-1] < lo:
        print(0)
    # Print result
    else:
        print(bin_search_r(cards, hi) - bin_search_l(cards, lo) + 1)
    
    