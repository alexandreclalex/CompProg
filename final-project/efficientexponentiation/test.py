from main import search
import time

TIMELIMIT = 2
n = 750
max_time = 0
while True:
    bin_string = str(bin(n))[2:]
    chain = [1]
    upper_bound = len(bin_string) + len([x for x in bin_string if x == '1']) - 2
    num_ones = len([x for x in bin_string if x == '1'])
    if num_ones <= 8:
        print(n, upper_bound)
        chain = [1]
        
        start = time.time()
        search(chain, n, upper_bound)
        elapsed = time.time() - start
        if elapsed > max_time:
            max_time = elapsed
        if elapsed > TIMELIMIT:
            print(n, upper_bound, num_ones, elapsed)
            break
    n += 1
    
print(max_time)