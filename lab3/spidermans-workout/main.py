cases = int(input())

for _ in range(cases):
    # Read in input
    moves = int(input())
    movements = [int(val) for val in input().split(" ")]
    num_movements = len(movements)
    
    # Determine the total distance, and the top possible valid distance (half of total)
    total_distance = sum(movements)
    top_distance = (total_distance // 2) + 1

    # If the total distance is odd, we cannot return to the ground
    if total_distance % 2 != 0:
        print("IMPOSSIBLE")
        continue

    # Initialize two grids - one for value, one for recording moves
    state = []
    moves = []
    for i in range(num_movements + 1):
        state_row = []
        move_row = []
        for j in range(top_distance):
            state_row.append(total_distance)
            move_row.append("")
        state.append(state_row)
        moves.append(move_row)

    # Set our initial state, and initialize the move list
    state[0][0] = 0

    # Populate the state table by filling every value
    for row in range(num_movements):
        movement = movements[row]

        # For each column, determine the most optimal path to reach each value
        for col in range(top_distance):
            min_val = state[row][col - movement] if col - movement >= 0 else total_distance
            max_val = state[row][col + movement] if col + movement < top_distance else total_distance

            # Calculate the most effective path to get to this position
            state[row + 1][col] = min(max(col, min_val), max_val)   

            # Determine which move was made
            if min_val != total_distance and max(col, min_val) < max_val:
                # We moved from the left
                moves[row + 1][col] = moves[row][col - movement] + "U"
            elif max_val != total_distance:
                # We moved from the right
                moves[row + 1][col] = moves[row][col + movement] + "D"

    # Print solution
    if state[-1][0] == total_distance:
        print("IMPOSSIBLE")
    else:
        print(moves[-1][0])
