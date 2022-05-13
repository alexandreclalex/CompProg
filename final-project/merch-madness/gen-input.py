import random


X_MIN = 20
Y_MIN = 20

X_MAX = 1000
Y_MAX = 1000

NUM_STORES_MAX = 100
STORE_CAPACITY_MAX = 25

NUM_PEOPLE_MAX = 1000


def get_new_location(coords, x_max, y_max):
    # Start with no valid location picked
    valid_loc = False

    # Iterate to find valid x and y
    while not valid_loc:
        # Determine location
        x = int(random.random() * x_max)
        y = int(random.random() * y_max)

        # Check if coordinate is valid
        if not coords[y][x]:
            valid_loc = True
            coords[y][x] = True

            # Return the valid coordinates
            return (x, y)


with open("generated_input.txt", "w") as f:
    # Determine the x and y bounds
    city_width = max(int(random.random() * X_MAX), X_MIN)
    city_height = max(int(random.random() * Y_MAX), Y_MIN)

    f.write(f"{city_width} {city_height}\n")

    # Keep track of the remaining locations in the city
    total_locations = city_width * city_height
    remaining_locations = total_locations

    # Create a dictionary to track which locations have been used
    used_coords = []

    for i in range(city_height + 1):
        used_coords.append([False] * (city_width + 1))

    # Determine the number of stores, making sure there is at least 1 person
    num_stores = NUM_STORES_MAX#min(int(random.random() * NUM_STORES_MAX), (remaining_locations - 1))

    f.write(f"{num_stores}\n")

    # Generate stores to match quantity
    for i in range(num_stores):
        # Determine a starting location
        (x, y) = get_new_location(used_coords, city_width, city_height)

        # Determine stock quantity
        capacity = STORE_CAPACITY_MAX#int(random.random() * STORE_CAPACITY_MAX)

        f.write(f"{i} {x} {y} {capacity}\n")

        # Decrement the remaining count when a store is added
        remaining_locations -= 1

    # Determine the number of people
    num_people = NUM_PEOPLE_MAX#min(int(random.random() * NUM_PEOPLE_MAX), remaining_locations)

    f.write(f"{num_people}\n")

    # Generate the locations of people
    for i in range(num_people):
        # Determine a starting location
        (x, y) = get_new_location(used_coords, city_width, city_height)

        f.write(f"{x} {y}\n")
