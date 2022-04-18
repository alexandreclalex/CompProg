import sys

authors = []
connections = dict()

inline = sys.stdin.readline()[:-1]
while inline != '':
    tokens = inline.split(' ')
    authors.append(tokens[0])
    for elem in tokens:
        connections[elem] = set(tokens)
        connections[elem].remove(elem)
    inline = sys.stdin.readline()[:-1]

def dfs(connections, node, visited, target, path):
    if node == target:
        return len(path)
    if target in connections[node]:
        return 1 + len(path)
    path.append(node)
    visited.append(node)
    min_len = 1000000
    for connection in connections[node]:
        if connection not in visited:
            length = dfs(connections, connection, visited, target, path[:])
            if length < min_len:
                min_len = length
    return min_len

for author in authors:
    e_num = dfs(connections, 'PAUL_ERDOS', [], author, [])
    if e_num == 1000000:
        print(author+' no-connection')
    else:
        print(author + ' ' + str(e_num))