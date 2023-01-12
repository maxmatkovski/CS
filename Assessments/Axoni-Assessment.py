from collections import defaultdict

# declare test variable
flights = """
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
"""

for flight in flights.splitlines():
    cities = flight.split(" -> ")
print(cities)

def find_shortest_path(flights, origin, desination):

    # create graph to represent the flights
    graph = defaultdict(list)
    for flight in flights.splitlines():
        cities = flight.split(" ")