from queue import PriorityQueue

# A-star defined: f(n) = g(n) + h(n)
# g(n) is cost to reach node from start node.
# h(n) is estimated cost to reach goal from node.

map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Craiova': ['Rimnicu Vilcea', 'Drobeta', 'Pitesti'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
}
# h(n) values
heuristic_val = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# To calculate cost, g(n) values
cost = {
    ("Arad", "Zerind"): 75, ("Oradea", "Zerind"): 71,
    ("Arad", "Timisoara"): 118, ("Timisoara", "Lugoj"): 111,
    ("Mehadia", "Lugoj"): 70, ("Mehadia", "Drobeta"): 75,
    ("Drobeta", "Craiova"): 120, ("Arad", "Sibiu"): 140,
    ("Oradea", "Sibiu"): 151, ("Sibiu", "Rimnicu Vilcea"): 80,
    ("Sibiu", "Fagaras"): 99, ("Pitesti", "Rimnicu Vilcea"): 97,
    ("Pitesti", "Bucharest"): 101, ("Iasi", "Neamt"): 87,
    ("Fagaras", "Bucharest"): 211, ("Vaslui", "Iasi"): 92,
    ("Urziceni", "Bucharest"): 85, ("Urziceni", "Vaslui"): 142,
    ("Rimnicu Vilcea", "Craiova"): 146, ("Craiova", "Pitesti"): 138,
    ("Bucharest", "Giurgiu"): 90, ("Urziceni", "Hirsova"): 98,
    ("Eforie", "Hirsova"): 86
}


visited_cities = {}     # To keep track of visited cities
parent = {}     # To keep a track of parent of each city
astar_search_output = []      # To store the order of bfs traversal
priority_queue = PriorityQueue()    # Priority Queue instead of ordinary queue for A* algorithm
isCityFound = True  # To check if the city has been found or not, set is to True by default

# To initialize the map
for city in map.keys():
    visited_cities[city] = False    # No city has been visited, hence all values are False
    parent[city] = None     # No city has been visited, hence parent is Null for now

start_city = input("Enter start city:\n")   # Take input of the start city
if not start_city in map:   # Check if the start city actually exists on the map
    print("The city does not exist on the map!")
    exit()

goal_city = "Bucharest" # Goal city is set to Bucharest

visited_cities[start_city] = True   # Mark Arad as a visited city to avoid infinite loop
priority_queue.put((0, start_city))   # Put the starting city in the priority queue with f(n) = 0
    # Parent city remains Null for the starting city

# Loop to assign parent and child node by implementing A* search algorithm
while True:

    if priority_queue.empty():   # If priority queue is empty, the city is not present in the tree
        isCityFound = False     # Set isCityFound as false and break the loop
        break

    else:
        current_cost, current_city = priority_queue.get()  # Pops and the first element of the priority queue
                                                        # And returns it as the current_city along with its f(n) value
        print(current_cost)
        if (current_city == goal_city):  # Check if the current city is the goal city, i.e., Bucharest
            astar_search_output.append((current_city))  # If so, add this to the search output list
            break  # Break the loop as we have already reached the goal city
        astar_search_output.append(current_city)  # Else, just add the current city to the list and continue

        for frontier in map[current_city]:  # Explore the frontier (child nodes) of the current city
            city_order1 = (current_city, frontier)  # To find the cost of two adjacent cities in the path
            city_order2 = (frontier, current_city)  # Two variables as the cities might be in different order
            if city_order1 in cost:
                gn = cost[city_order1]
            elif city_order2 in cost:
                gn = cost[city_order2]
            hn = heuristic_val[frontier]    # Find the value of hn (Heuristic value)
            fn = gn + hn    # Calculate the value of fn
            # Proceed only if the frontier has not been visited before and if the go
            if not visited_cities[frontier]:  # Proceed only if the frontier has not been visited before
                visited_cities[frontier] = True  # Mark the frontier as visited to avoid infinite loops
                parent[frontier] = current_city  # Set the current city as the parent of the frontier
                priority_queue.put((fn, frontier))  # Enqueue the frontier to the queue according to the value of fn
                # And continue the algorithm


if isCityFound == False:    # Check if the city has been found or not
    print(f"There is no existing path between {start_city} and {goal_city}")
    exit()      # Exit the program if the city has not been found

path = []   # Create empty list to display the shortest path
total_cost = 0
# Loop to find the shortest path
while goal_city is not None:    # Continue till the goal city does not exist
    path.append(goal_city)      # Add the current goal_city to the path
    goal_city = parent[goal_city]   # Change the goal city to its parent
path.reverse()  # Reverse the list
print("\nThe shortest path using A* search algorithm is:")
print(path)

# To calculate cost of the path
total_cost = 0
size = len(path)
for i in range(0, size - 1):
    cities_order1 = (path[i], path[i + 1])  # To find the cost of two adjacent cities in the path
    cities_order2 = (path[i + 1], path[i])  # Two variables as the cities might be in different order
    if cities_order1 in cost:
        total_cost = total_cost + cost[cities_order1]
    elif cities_order2 in cost:
        total_cost = total_cost + cost[cities_order2]

print("\nTotal cost =", total_cost)

print("\nThe cities visited by the algorithm during the search were:")
print(astar_search_output)
