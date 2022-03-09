
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
                    l2.append(int(line[j]))

                l1.append(l2)

            game_grids[i] = l1

    return game_grids

def search_neighbors(board, color, x=0, y=0, checked=[], occurrences=[], current_arr=[]):
    #print(f"Searching ({x}, {y})")
    size = len(board[0])

    if (x >= 0 and x < size) and (y >= 0 and y < size) and (x,y) not in checked:
        checked.append((x,y))

        current_color = board[y][x]
       
        if current_color == color:
            current_arr.append((x, y))

            (occurrences, current_arr) = search_neighbors(board, color, x, y-1, checked, occurrences, current_arr)

            #(occurrences, current_arr) = search_neighbors(board, color, x+1, y-1, checked, occurrences, current_arr)
            
            (occurrences, current_arr) = search_neighbors(board, color, x+1, y, checked, occurrences, current_arr)
            
            #(occurrences, current_arr) = search_neighbors(board, color, x+1, y+1, checked, occurrences, current_arr)
            
            (occurrences, current_arr) = search_neighbors(board, color, x, y+1, checked, occurrences, current_arr)
            
            #(occurrences, current_arr) = search_neighbors(board, color, x-1, y+1, checked, occurrences, current_arr)
            
            (occurrences, current_arr) = search_neighbors(board, color, x-1, y, checked, occurrences, current_arr)
            
            #(occurrences, current_arr) = search_neighbors(board, color, x-1, y-1, checked, occurrences, current_arr)
        else:
            occurrences.append(current_color)

    return occurrences, current_arr


def play_game(board):
    steps = {}

    for i in range(5):
        occurrences, current_arr = search_neighbors(board, board[0][0], 0, 0, [], [], [])

        if len(current_arr) == len(board[0]) ** 2:
            return steps

        occurrences_dict = {}
        for element in occurrences:
            occurrences_dict[element] = occurrences_dict.get(element, 0) + 1

        max_val = (1, 0)
        for key in occurrences_dict.keys():
            val = occurrences_dict[key]
            if val > max_val[1]:
                max_val = (key, val) 
            elif val == max_val[1] and key < max_val[0]:
                max_val = (key, val)

        for (x, y) in current_arr:
            board[y][x] = max_val[0]

        steps[max_val[0]] = steps.get(max_val[0], 0) + 1



def main():
    game_grids = read_file("lab1/flood-it/sample-input.txt")
    
    for game in game_grids.keys():
        game_board = game_grids[game]

        steps = play_game(game_board)

        print(steps)


if __name__ == "__main__":
    main()