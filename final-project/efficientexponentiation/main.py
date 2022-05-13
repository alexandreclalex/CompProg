import sys

def search(chain, exponent, maxdepth):
    last = chain[-1]
    for i in range(len(chain)):
        
        # Found exponent
        if chain[len(chain) - 1 - i] + last == exponent:
            return True
        
        # Keep searching
        chain.append(chain[len(chain) - 1 - i] + last)
        if len(chain) < maxdepth and chain[len(chain) - 1 - i] + last < exponent and search(chain, exponent, maxdepth):
            return True
        chain.pop()
        
if __name__ == '__main__':
    n = int(sys.stdin.readline())

    bin_string = str(bin(n))[2:]
    
    # Use binary method to find upper bound
    upper_bound = len(bin_string) + len([x for x in bin_string if x == '1']) - 2

    for depth in range(0, upper_bound+1):
        chain = [1]
        
        # DFS
        if search(chain, n, depth):
            print(len(chain))
            exit(0)
    print(upper_bound)
