# Popularity Contest

# Edge cases
# N  (2≤N≤1000), the number of your friends,
# M (0≤M≤N(N−1)/2), the number of friendships.
# 1 ≤ a ≠ b ≤ N, denoting that the a’th and b’th of your friends are friends.

# Input Section: friends and number of friendships
M, N = 0, 0
condition_met = False
while not condition_met:
    first_line = input().split(' ')
    N = int(first_line[0])
    M = int(first_line[1])
    if 2 <= N <= 1000 and 0 <= M <= (N*(N-1)/2):
        condition_met = True

# Creating popularity_score array
popularity_score = [0] * N

# Collecting pairs
for x in range(M):
    pair = input().split(' ')
    a = int(pair[0])
    b = int(pair[1])
    if 1 <= a <= N and 1 <= b <= N and a != b:
        popularity_score[a-1] += 1
        popularity_score[b-1] += 1

# Print output in a single line
for x in range(1, N+1):
    print(popularity_score[x-1] - x, end=" ")
