import sys

possible_vals = set()
remaining_vals = set()
min_len = 1000000000
min_len = 0


class Node:
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.children = []

    def add_child(self, val, end):
        self.children.add(Node(val))

    def check_child(self, val):
        return next((val for val in self.children), None)


class Trie:
    def __init__(self):
        self.root = Node()


if __name__ == '__main__':       
    num_lines = int(sys.stdin.readline()[:-1])

    clues = set()

    for i in range(num_lines):
        clue_binary_str = sys.stdin.readline().strip('\n')
        clue_val = int(clue_binary_str, 2)
        # max_val = int(''.join(["1"]*len(clue_binary_str)), 2)

        min_len = min(min_len, len(clue_binary_str))
        max_len = max(max_len, len(clue_binary_str))

    for i in range(min_len, max_len):


        # print(clue_val)
        # print(clue_val >> 1)

        print(len(clue_val))
        print(len(clue_val >> 1))

        for i in range(min_len, max_len):
            



        # if max_val > current_max:
        #     for j in range(max_val - current_max):
        #         possible_vals.add(j + current_max)

        #         if j + current_max != clue_val:
        #             remaining_vals.add(j + current_max)
        # else:
        #     remaining_vals.discard(clue_val)
