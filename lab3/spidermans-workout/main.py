cases = int(input())

for _ in range(cases):
    moves = int(input())
    distances = [int(val) for val in input().split(" ")]

    tree = [(distances[0], distances[0], distances[0], "U")] # (Value, Max, Path)
    edge_indexes = [0]
    next_indexes = []

    for i, diff in enumerate(distances[1:]):
        for tree_index in edge_indexes:
            (current, max_val, min_val, path) = tree[tree_index]

            tree.append((current - diff, max_val, min(min_val, current - diff), path + "D"))
            tree.append((current + diff, max(max_val, current + diff), min_val, path + "U"))

            next_indexes.append((2 * tree_index) + 1)
            next_indexes.append((2 * tree_index) + 2)

        edge_indexes = next_indexes
        next_indexes = []

    final_arr = list(filter(lambda x: x[0] == 0 and x[2] >= 0, tree[(2 * moves) - 1:]))

    print(final_arr)
    sorted_final_arr = sorted(final_arr, key=lambda x: x[1])

    print(sorted_final_arr[0][3]) if sorted_final_arr else print("IMPOSSIBLE")

