import sys
from heapq import heappop, heappush


total_stock = 0
stores = dict()
nearest_stores = dict()
stores_stock = dict()
people = []


def dist(x1, y1, x2, y2):
    """
    Compute Manhattan distance between two points
    """
    return abs(x1 - x2) + abs(y1 - y2)


def process_store():
    """
    Read in information about a store, and save the data to a dictionary for the (X, Y) of the store, mapped to it's ID. Additionally, save a separate dictionary with the store stock tied to it's ID.
    """
    # Declare global variable for modification
    global total_stock

    # Read in the ID, X, Y, and capacity of the store
    id, x, y, capacity = map(int, sys.stdin.readline().strip("\n").split(" "))

    # Save the store's location and capacity
    stores[id] = (x, y)
    stores_stock[id] = capacity
    
    # Increment total capacity
    total_stock += capacity


def map_stores():
    """
    Generate a sorted list from an origin store, to each of it's neighboring stores. The list is stored in a dict mapped to the origin store's ID, sorted by distance from the origin to the neighboring store.
    """
    # Iterate through all stores
    for i in stores.keys():
        # Ensure the current store has stock. If not, skip the store
        if stores_stock[i] == 0:
            continue

        # Pull out the X and Y of the store's location
        current_x, current_y = stores[i]
        
        # Iterate through all other stores
        for j in stores.keys():
            # If the two stores are different, and the other store has stock
            if i != j and stores_stock[j] > 0:
                # Pull out the X and Y of the other store's location
                other_x, other_y = stores[j]

                # Determine the distance between the stores
                distance = dist(current_x, current_y, other_x, other_y)

                # Save a priority queue of nearest stores to the current store
                store_distances = nearest_stores.get(i, [])
                heappush(store_distances, (distance, j))

                nearest_stores[i] = store_distances


def process_person():
    """
    Read in the information for a person, and map them to their nearest store
    """
    # Read the X and Y coordinates for a person
    x, y = map(int, sys.stdin.readline().strip("\n").split(" "))

    # Create a tuple to store (distance, store ID) for the nearest store
    closest_store = (0, -1)

    # Iterate through each store
    for i in stores.keys():
        # Extract the store's X and Y location
        store_x, store_y = stores[i]

        # If the store has no stock, don't add it to the neighboring list
        if stores_stock[i] == 0:
            continue

        # Determine the distance to the store
        distance = dist(x, y, store_x, store_y)

        # If a closest store isn't saved, or this store is closer, save it's information
        if closest_store[1] == -1 or distance <= closest_store[0]:
            closest_store = (distance, i)

    # Create a priority queue based on distances to the nearest stores of each person
    heappush(people, closest_store)


def allocate_person(starting_time):
    """
    Run through the simulation until the next person reaches a store. Once reached, update the stock values, and return the amount of time taken to get the one person to the store.
    """
    # Get the distance and ID of the person closest to a store
    distance, id = heappop(people)

    # Check if the store's stock is 0
    if stores_stock[id] == 0:
        # Store a placeholder ID and distance for the next store to go to
        new_store_id = -1
        new_store_dist = 0

        # Keep looping through stores until the next one is found
        while new_store_id == -1:
            # Grab the nearest store to the current store
            (next_dist, next_id) = nearest_stores[id][0]
            
            # If the nearest store has no more stock
            if stores_stock[next_id] == 0:
                # Throw out nearest store as it has no stock
                _ = heappop(nearest_stores[id])
            else:
                # Set the new store as a target
                new_store_id = next_id
                new_store_dist = next_dist

        # Re-add person to the queue with a new distance, and a new store
        heappush(people, (new_store_dist + distance, new_store_id))
    else:
        # Decrement stock if the store has enough for the individual
        stores_stock[id] = stores_stock[id] - 1

    return distance - starting_time
        


def execute():
    """
    Run the primary logic to solve the problem.
    """
    # Pass through global variables for function modification
    global total_stock
    global stores
    global nearest_stores
    global stores_stock
    global people

    # Reset variables for unit tests
    total_stock = 0
    stores = dict()
    nearest_stores = dict()
    stores_stock = dict()
    people = []

    # Read in the grid size
    _ = map(int, sys.stdin.readline().strip("\n").split(" "))
    
    # Read in the total number of stores
    num_stores = int(sys.stdin.readline().strip("\n"))

    # Process each of the stores
    for _ in range(num_stores):
        process_store()

    # Read in the total number of people
    num_people = int(sys.stdin.readline().strip("\n"))

    # Check to make sure there is enough capacity. If not, end early.
    if num_people > total_stock:
        print("out of stock")
        return 0

    # Process each of the people
    for _ in range(num_people):
        process_person()

    # Map all of the stores for optimized look-ups later
    map_stores()

    # Keep track of the current time that has passed
    current_time = 0

    # Run through each person in the simulation
    while len(people) > 0:
        current_time += allocate_person(current_time)

    # Print out the total time to get everyone to a store
    print(current_time)

    return 0


if __name__ == "__main__":
    execute()
