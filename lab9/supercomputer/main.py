import sys

class FenwickTree:
    def __init__(self, n):
        self.arr = [False]*n
        self.sum_tree = [0]*(n+1)
        
    def flip(self, i):
        value = -1 if self.arr[i-1] else 1
        self.arr[i-1] = not self.arr[i-1]
        while i <= len(self.arr):
            self.sum_tree[i] += value
            i += i & (-i)
    
    def sum(self, l, r):
        return self.__single_sum(r) - (self.__single_sum(l-1) if l > 1 else 0)
    
    def __single_sum(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & (-i)
        return s

if __name__ == '__main__':
    bits, queries = map(int, sys.stdin.readline().split())
    tree = FenwickTree(bits)
    
    for _ in range(queries):
        tokens = sys.stdin.readline().split()
        if tokens[0] == 'F':
            tree.flip(int(tokens[1]))
        else:
            print(tree.sum(int(tokens[1]), int(tokens[2])))