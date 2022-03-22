def parse_inputs():
    """
    Parse the inputs from stdin
    """
    input_vals = input()
    input_arr = input_vals.split(" ")

    # Parse out each of the variables
    num_rides = int(input_arr[0])
    num_a = int(input_arr[1])
    num_b = int(input_arr[2])
    num_c = int(input_arr[3])

    # Return all inputs
    return (num_rides, num_a, num_b, num_c)


def next_ride(options: dict, total: int, selected: str, depth: int):
    """
    Determine the choices available after riding an additional ride at the park
    """
    # Determine what types of rides we can use (different type than the current selected type)
    keys = [key for key in options.keys() if key != selected]
    
    # Base case - ensure we don't go pass the total number of rides
    if depth == total:
        return 1

    # For each type of ride, expand the tree of possibilities further
    sum = 0
    for key in keys:
        # Multiply the number of rides in the type by the number of rides that can follow
        sum += options[key] * next_ride(options, total, key, depth + 1)

    # Return the total number of possibilities
    return sum


if __name__ == "__main__":
    # Parse inputs
    (num_rides, a, b, c) = parse_inputs()

    # Define ride types and quantities
    options_dict = {
        'A': a,
        'B': b,
        'C': c
    }

    # Determine the total number of possibilities
    total = next_ride(options_dict, num_rides, None, 0)

    # Print the total possibilities in the format for the problem
    print(total % (10 ** 9 + 7))
