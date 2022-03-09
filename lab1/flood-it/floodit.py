class Node:
    def __init__(self, value: int) -> None:
        self.neighbors = list()
        self.value = value
    
    def add_neighbor(self,node) -> None :
        self.neighbors.append(node)

    def get_best(self) -> int:
        diff_nodes = self.get_diff_neighbors(set())
        values = [0]*7
        for node in diff_nodes:
            values[node.value] += 1
        
        return values.index(values.max)

    def get_neighbors(self, visited: set) -> None:
        for node in self.neighbors:
            visited.add(self)
            if node not in visited:
                if node.value == self.value:
                    node.get_diff_neighbors(visited)
                else:
                    visited.add(node)
    
    def __repr__(self) -> str:
        return str(self.value)

if __name__ == '__main__':
    num_boards = int(input())
    for boardnum in range(num_boards):
        width = int(input())
        node_arr = []
        for i in range(width):
            node_arr.append(list(map(Node, map(int, input()))))
        print(node_arr)