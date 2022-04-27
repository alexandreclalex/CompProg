import sys

n = int(sys.stdin.readline()[:-1])

s = list(sys.stdin.readline()[:-1])

moves = 0

# if s[0] == 'B' and s[1] == 'A':
#     s[0] = 'A'
#     moves+=1
    
for i in range(1, n-1):
    if s[i-1] == s[i+1] and s[i-1] != s[i]:
        s[i] = s[i-1]
        moves += 1

if s[n-1] != s[n-2] and s[n-1] != 'A':
    s[n-1] = s[n-2]
    moves += 1
    
current = s[0]
for i in range(len(s)):
    if s[i] != current:
        current = s[i]
        moves += 1

if current == 'B':
    moves += 1
    
# if s[0] != 'A':
#     moves += 1
    
print(moves)
    