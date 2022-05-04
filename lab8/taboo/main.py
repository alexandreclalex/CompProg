import sys

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Trie:
    def __init__(self) -> None:
        self.root = Node('')
    
    def insert(self, value):
        next_node = root
        for char in value:
            if char =='0' and next_node.left is None:
                pass
                

if __name__ == '__main__':       
    n = int(sys.stdin.readline()[:-1])

    root = Node(None)
