

def parse_inputs():
    input_vals = input()
    input_arr = input_vals.split(" ")

    num_rides = int(input_arr[0])
    num_a = int(input_arr[1])
    num_b = int(input_arr[2])
    num_c = int(input_arr[3])

    return (num_rides, num_a, num_b, num_c)


def next_ride(options: dict, total: int, selected: str, depth: int):
    keys = [key for key in options.keys() if key != selected]
    
    if depth > total:
        return 1

    sum = 0
    for key in keys:
        if selected is not None:
            sum = options[selected] * next_ride(options, total, key, depth + 1)
        else:
            sum += next_ride(options, total, key, depth + 1)

    return sum


if __name__ == "__main__":
    (num_rides, a, b, c) = parse_inputs()

    options_dict = {
        'A': a,
        'B': b,
        'C': c
    }

    total = next_ride(options_dict, num_rides, None, 0)

    print(total)

