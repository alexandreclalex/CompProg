import sys
def do_it():
    num_cities, num_lines = list(map(int, sys.stdin.readline()[:-1].split(' ')))

    adj_list = []
    for i in range(num_cities):
        adj_list.append([None]*num_cities)
        
    for i in range(1, num_lines + 1):
        x, y = list(map(int, sys.stdin.readline()[:-1].split(' ')))
        adj_list[x-1][y-1] = i
        adj_list[y-1][x-1] = i

    path = []
    for i in range(num_cities-1):
        if adj_list[i][i+1] is None:
            print('impossible')
            return []
        else:
            path.append(adj_list[i][i+1])

    if adj_list[num_cities - 1][0] is None:
        print('impossible')
        return []
    else:
        path.append(adj_list[num_cities - 1][0])
    return path
        
for elem in do_it():
    print(elem)
