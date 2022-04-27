import sys

def get_digit(n):
    result = 1
    while n > 0:
        temp = n%10
        if temp > 1:
            result *= temp
        n //= 10
    return result if result < 10 else get_digit(result)

def get_digit_one_step(n):
    result = 1
    while n > 0:
        temp = n%10
        if temp > 1:
            result *= temp
        n //= 10
    return result

cache = dict()
def populate_cache(n=1):
    if n not in cache and n <= 10**15:
        cache[n] = get_digit(n)
        for factor in [2, 3, 5, 7]:
            populate_cache(n * factor)

a, b = map(int, sys.stdin.readline().split())

populate_cache()
result = [0]*9
for i in range(a, b+1):
    next_val = cache[get_digit_one_step(i)]
    print(next_val)
    result[next_val - 1] += 1

print(' '.join(map(str, result)))
