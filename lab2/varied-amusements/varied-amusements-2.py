def parse_inputs():
    input_vals = input()
    input_arr = input_vals.split(" ")

    num_rides = int(input_arr[0])
    num_a = int(input_arr[1])
    num_b = int(input_arr[2])
    num_c = int(input_arr[3])

    return (num_rides, num_a, num_b, num_c)


if __name__ == "__main__":
    (num_rides, a, b, c) = parse_inputs()

    current_dict = {
        "abc": a + b + c,
        "ab": a + b,
        "bc": b + c,
        "ac": a + c
    }

    next_dict = {
        "abc": ["ab", "bc", "ac"],
        "ab": ["bc", "ac"],
        "bc": ["ab", "ac"],
        "ac": ["ab", "bc"]
    }

    total = current_dict["abc"]
    keys = next_dict["abc"]
    next_keys = []

    for i in range(num_rides - 1):
        for key in keys:
            total *= current_dict[key]
            next_keys += next_dict[key]

        keys = next_keys
        next_keys = []

    print(total % (10 ** 9 + 7))
