from queue import Queue

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
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest'],
    'Craiova': ['Rimnicu Vilcea', 'Drobeta'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
    'London': ['Liverpool', 'Manchester'],  # For checking if "city not found" portion works
    'Manchester': ['Liverpool', 'London'],  # For checking if "city not found" portion works
    'Liverpool': ['Manchester', 'London'],  # For checking if "city not found" portion works
}

# To calculate cost
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


visited_cities = {}     # To keep a track of visited cities
parent = {}     # To keep a track of parent of each city
dfs_output = []     # To store the order of dfs traversal

# To initialize the map
for city in map.keys():
    visited_cities[city] = False    # No city has been visited, hence all values are False
    parent[city] = None       # No city has been visited, hence parent is Null for now

# Depth First Search Algorithm to assign parent and child node
def depth_first(current_city, goal_city):
    if current_city == goal_city:   # Check if current city is the goal city
        dfs_output.append(current_city)     # If so, then add current city to the traversal list
        return(dfs_output)      # Return the traversal list and exit the function
    visited_cities[current_city] = True     # Otherwise, mark the current city as visited
    dfs_output.append(current_city)     # Add the current city to the traversal list

    # Loop to implement depth first search algorithm to assign parent and child node
    for frontier in map[current_city]:      # Explore the frontier (child nodes) of the current city
        if not visited_cities[frontier]:    # Proceed only if the frontier has not been visited before
            parent[frontier] = current_city     # Set the current city as the parent of the frontier
            dfs_tree = depth_first(frontier, goal_city)     # Recursively call the depth first function
            if dfs_tree is not None:    # Check if the goal has been found
                return dfs_tree         # If no, then return the result

    visited_cities[current_city] = True     # Mark the current city as visited to avoid infinite loops
    return None     # Return none if the goal is not found

start_city = input("Enter start city:\n")   # Take input of the start city
if not start_city in map:   # Check if the start city actually exists on the map
    print("The city does not exist on the map!")
    exit()
goal_city = input("Enter goal city\n")   # Take input of the goal city
if not start_city in map:    # Check if the start city actually exists on the map
    print("The city does not exist on the map!")
    exit()

output = depth_first(start_city, goal_city)     # Call the depth first function

if output is None:      # Check if the goal has been found the function
    print("DFS did not find a path")
    exit()      # Exit the program if goal has not been found

path = []   # Create empty list to display the shortest path
# Loop to find the shortest path
while goal_city is not None:    # Continue till the goal city does not exist
    path.append(goal_city)      # Add the current goal_city to the path
    goal_city = parent[goal_city]       # Change the goal city to its parent
path.reverse()  # Reverse the list
print("\nThe shortest path using breadth first search algorithm is:")
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
print(dfs_output)
