
def read_file(path):
    game_grids = {}
    with open(path, 'r') as f:
        num_test_cases = int(f.readline())

        for i in range(num_test_cases):
            grid_size = int(f.readline())

            l1 = []
            for _ in range(grid_size):
                l2 = []
                line = f.readline()

                for j in range(grid_size):
                    l2.append(line[j])

                l1.append(l2)

            game_grids[i] = l1

    return game_grids

def search_neighbors(board, color, x=0, y=0, checked=[], occurrences_dict={}, current_arr=[]):
    current_color = board[y][x]
    size = len(board[0])

    if (x,y) not in checked:
        checked.append(x,y)

        if current_color == color:
            current_arr.append((x, y))
        else:
            occurrences_dict[current_color] = occurrences_dict.get(current_color, 0) + 1

        if (y - 1) >= 0: # Search top center
            search_neighbors(board, color, x, y-1, occurrences_dict, current_arr)

        if (y - 1) >= 0 and (x + 1) <= size: # Search top right
            search_neighbors(board, color, x+1, y-1, occurrences_dict, current_arr)

        if (x + 1) <= size: # Search center right
            search_neighbors(board, color, x+1, occurrences_dict, current_arr)

        if (y + 1) <= size and (x + 1) <= size: # Search bottom right
            search_neighbors(board, color, x+1, y+1, occurrences_dict, current_arr)

        if (y + 1) <= size: # Search bottom center
            search_neighbors(board, color, x, y+1, occurrences_dict, current_arr)

        if (y + 1) <= size and (x - 1) >= 0: # Search bottom left
            search_neighbors(board, color, x-1, y+1, occurrences_dict, current_arr)

        if (x - 1) >= 0: # Search center left
            search_neighbors(board, color, x-1, y, occurrences_dict, current_arr)

        if (y - 1) >= 0 and (x - 1) >= 0: # Search top left
            search_neighbors(board, color, x-1, y-1, occurrences_dict, current_arr)

    return occurrences_dict, current_arr


    


def play_game(board):
    steps = {}

    while True:
        occurrences_dict, current_arr = search_neighbors(board, board[0][0])

        if len(current_arr) == len(board[0]) ** 2:
            return steps

        max_val = (1, 0)
        for key in occurrences_dict.keys():
            val = occurrences_dict[key]
            if val > max_val[1]:
                max_val = (key, val) 

        for (x, y) in current_arr:
            board[y][x] = max_val[0]

        steps[max_val[0]] = steps.get(max_val[0], 0) + 1



def main():
    game_grids = read_file("sample-input.txt")
    
    for game in game_grids.keys():
        game_board = game_grids[game]

        play_game(game_board)


if __name__ == "__main__":
    main()