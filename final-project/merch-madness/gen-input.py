import random

from sqlalchemy import false


X_MAX = 1000
Y_MAX = 1000

NUM_STORES_MAX = 100
STORE_CAPACITY_MAX = 100

NUM_PEOPLE_MAX = 1000

with open("generated_input.txt", "w") as f:
    # Determine the x and y bounds
    city_width = 100 #int(random.random() * X_MAX)
    city_height = 100 #int(random.random() * Y_MAX)

    f.write(f"{city_width} {city_height}\n")

    # Create a dictionary to track which locations have been used
    used_coords = dict() # used_coords[X] = Y

    # Determine the number of stores
    num_stores = 10 #int(random.random() * NUM_STORES_MAX)

    f.write(f"{num_stores}\n")

    # Generate stores to match quantity
    for i in range(num_stores):
        valid_loc = False

        x = -1
        y = -1

        while not valid_loc:
            # Determine location
            x = int(random.random() * X_MAX)
            y = int(random.random() * Y_MAX)

            # Check if coordinate is valid
            if used_coords.get(x) == None or y not in used_coords.get(x):
                valid_loc = True
                used_coords[x] = y

        # Determine stock quantity
        capacity = int(random.random() * STORE_CAPACITY_MAX)

        f.write(f"{x} {y} {capacity}\n")

    # Determine the number of people
    num_people = 100 #int(random.random() * NUM_PEOPLE_MAX)

    # Generate the locations of people
    for i in range(num_people):

  