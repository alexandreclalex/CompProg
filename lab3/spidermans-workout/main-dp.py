cases = int(input())

for _ in range(cases):
    moves = int(input())
    distances = [int(val) for val in input().split(" ")]

    total_distance = sum(distances)
    top_distance = (total_distance // 2) + 1

    

