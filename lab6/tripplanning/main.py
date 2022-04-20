import sys

# Read in the number of cities, and number of train lines
num_cities, num_lines = list(map(int, sys.stdin.readline()[:-1].split(' ')))

# Create sets to store the cities that still need to be connected
remaining_connections = set()
established_connections = set()

# Add all endpoints to the set
for i in range(1, num_cities + 1):
    remaining_connections.add(i)

# Read in each of the input lines (offset by one to match line index)
for i in range(1, num_lines + 1):
    # Determine the from and to nodes of the train line
    from_node, to_node = list(map(int, sys.stdin.readline()[:-1].split(' ')))

    # Find the minimum and maximum values of the two nodes
    min_val = min(from_node, to_node)
    max_val = max(from_node, to_node)

    # Keep track of if the min and max trips have been added
    added_min = False
    added_max = False

    # If the min is 1, and the max is equal to the number of cities, this is the ride back
    if min_val == 1 and max_val == num_cities:
        # Create an established connection between the end and the beginning (at the end of the set)
        established_connections.add((num_cities, i))
        added_min = True 
    
    # If the train line moves a single node (increases by one)    
    if (max_val - min_val == 1 and max_val in remaining_connections):
        # Add the destination to the established connections, with the line that takes you there
        established_connections.add((max_val - 1, i))
        added_max = True

    # Remove the destination from the connections
    if added_min:
        remaining_connections.discard(min_val)
    
    # Remove the destination from the connections
    if added_max:
        remaining_connections.discard(max_val)    

# Check if there are remaining connections that weren't made
if len(remaining_connections) > 0:
    # Print impossible if so
    print('impossible')
else:
    # Sort the established connections based on their end node (putting the end->beginning path last)
    established_connections = sorted(established_connections, key=lambda x: x[0])

    # Print out the connections
    for conn in established_connections:
        print(conn[1])
