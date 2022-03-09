class Node:
    def __init__(self, value: int) -> None:
        self.neighbors = list()
        self.value = value
    
    def add_neighbor(self,node) -> None :
        self.neighbors.append(node)

    def play_best(self) -> int:
        diff_nodes = set()
        diff_nodes = self.get_diff_neighbors(diff_nodes)
        values = [0]*7
        for node in diff_nodes:
            values[node.value] += 1
        values[self.value] = 0

        old_value = self.value
        new_value = values.index(max(values))
        for node in diff_nodes:
            if node.value == old_value:
                node.value = new_value
        return new_value

    def score(self, target:int, visited, curr_score):
        visited.add(self)
        for node in self.neighbors:
            if node not in visited:
                if node.value == self.value or node.value == target:
                    visited, curr_score = node.score(target, visited, curr_score)
                if node.value == target:
                    curr_score += 1
        return visited, curr_score

    def get_same_neighbors(self, visited) -> set:
        visited.add(self)
        for node in self.neighbors:
            if node not in visited and node.value == self.value:
                visited = node.get_same_neighbors(visited)
        return visited

    def get_diff_neighbors(self, visited: set) -> set:
        visited.add(self)
        for node in self.neighbors:
            if node not in visited:
                if node.value == self.value:
                    visited = node.get_diff_neighbors(visited)
                else:
                    visited = node.get_same_neighbors(visited)
        return visited
    
    def __repr__(self) -> str:
        return str(self.value)

def arrprint(arr):
    for row in arr:
        print(row)
    print()

if __name__ == '__main__':
    num_boards = int(input())
    for boardnum in range(num_boards):
        width = int(input())
        node_arr = []
        for i in range(width):
            node_arr.append(list(map(Node, map(int, input()))))
        
        #Populate Nodes
        for i in range(width):
            for j in range(width):
                if i - 1 >= 0:
                    node_arr[i][j].add_neighbor(node_arr[i-1][j])
                if j - 1 >= 0:
                    node_arr[i][j].add_neighbor(node_arr[i][j-1])
                if i + 1 < width:
                    node_arr[i][j].add_neighbor(node_arr[i+1][j])
                if j + 1 < width:
                    node_arr[i][j].add_neighbor(node_arr[i][j+1])

        moves = [0]*6
        next_move = node_arr[0][0].play_best()
        while next_move != 0:
            moves[next_move - 1] += 1
            next_move = node_arr[0][0].play_best()

        print(sum(moves))
        print(*moves)
