
def read_input():
    game_grids = {}
    num_test_cases = int(input())

    for i in range(num_test_cases):
        grid_size = int(input())

        l1 = []
        for _ in range(grid_size):
            l2 = []
            line = input()

            for j in range(grid_size):
                l2.append(int(line[j]))

            l1.append(l2)

        game_grids[i] = l1

    return game_grids

def generate_path(board, color, x=0, y=0, checked=set(), path=set(), neighbors=set()):
    size = len(board[0])

    if (x >= 0 and x < size) and (y >= 0 and y < size) and (x,y) not in checked:
        checked.add((x,y))

        current_color = board[y][x]

        if current_color == color:
            path.add((x,y))

            (checked, path, neighbors) = generate_path(board, color, x, y-1, checked, path, neighbors)
            (checked, path, neighbors) = generate_path(board, color, x+1, y, checked, path, neighbors)
            (checked, path, neighbors) = generate_path(board, color, x, y+1, checked, path, neighbors)
            (checked, path, neighbors) = generate_path(board, color, x-1, y, checked, path, neighbors)
        else:
            neighbors.add((x,y))

    return checked, path, neighbors


def play_game(board):
    steps = {}

    while True:
        (checked, path, neighbors) = generate_path(board, board[0][0], 0, 0, set(), set(), set())

        # If all squares are colored the same, end game
        if len(path) == len(board[0]) ** 2:
            return steps

        neighboring_colors = {}

        visited = path.copy()
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            color = board[y][x]

            (new_checked, new_path, _) = generate_path(board, color, x, y, visited.copy(), set(), set())

            visited = visited.union(new_path)

            neighboring_colors[color] = neighboring_colors.get(color, 0) + len(new_path)

        next_color = None
        max_val = max(neighboring_colors.values())

        for color in neighboring_colors.keys():
            if neighboring_colors[color] == max_val and (next_color is None or color < next_color):
                next_color = color

        for (x, y) in path:
            board[y][x] = next_color

        steps[next_color] = steps.get(next_color, 0) + 1


def main():
    game_grids = read_input()
    
    for game in game_grids.keys():
        game_board = game_grids[game]

        steps = play_game(game_board)

        steps_total = 0
        steps_str = ""

        for i in range(1, 7):
            steps_total += steps.get(i, 0)
            steps_str += f"{steps.get(i, 0)} "

        print(f"{steps_total}\n{steps_str}")


if __name__ == "__main__":
    main()