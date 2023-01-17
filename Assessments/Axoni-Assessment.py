def shortest_paths(flights, origin, destination):
    # Split the input string into a list of flights
    flights = flights.strip().split("\n")
    # Create an empty dictionary to store the flight connections
    connections = {}
    # Iterate through the list of flights
    for flight in flights:
        # Split the flight into a list of cities
        cities = flight.split(" -> ")
        # Iterate through the list of cities
        for i in range(len(cities)-1):
            # Check if the current city is already in the connections dictionary
            if cities[i] not in connections:
                # If not, add it as a key and set its value to a list of its connecting cities
                connections[cities[i]] = [cities[i+1]]
            else:
                # If it is, append the next city to the list of connecting cities
                connections[cities[i]].append(cities[i+1])
    
    # Check if either the origin or destination is not in the connections dictionary
    if origin not in connections or destination not in connections:
        return 'none'

    # Create a queue to store the paths to be checked
    queue = [[origin]]
    # Create a set to store the cities that have already been checked
    visited = set()
    # While the queue is not empty
    while queue:
        # Get the first path in the queue
        path = queue.pop(0)
        # Get the last city in the path
        city = path[-1]
        # If the city has not been visited yet
        if city not in visited:
            # Mark the city as visited
            visited.add(city)
            # If the city is the destination
            if city == destination:
                # Return the path
                return [path]
            # If the city is not the destination
            else:
                # Iterate through the connecting cities
                for connection in connections[city]:
                    # Create a new path with the connection added
                    new_path = list(path)
                    new_path.append(connection)
                    # Add the new path to the queue
                    queue.append(new_path)
    return 'none'


flights = """
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
"""

print(shortest_paths(flights, 'Amsterdam', 'London')) # 'none'