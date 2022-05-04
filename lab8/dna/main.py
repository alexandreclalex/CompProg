import sys

n = int(sys.stdin.readline()[:-1])

s = list(sys.stdin.readline()[:-1])

moves = 0

# Flip all ABA and BAB to AAA and BBB
for i in range(1, n-1):
    if s[i-1] == s[i+1] and s[i-1] != s[i]:
        s[i] = s[i-1]
        moves += 1

# If the last 2 chars are AB, flip the last bit
if s[n-1] != s[n-2] and s[n-1] != 'A':
    s[n-1] = s[n-2]
    moves += 1

# Keep track of distinct blocks to solve
current = s[0]
for i in range(len(s)):
    if s[i] != current:
        current = s[i]
        moves += 1

# If we end on a B, we need one more swap
if current == 'B':
    moves += 1
    
print(moves)
    