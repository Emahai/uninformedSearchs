import heapq  
from question2a import state_space_graph

def uniform_cost_search(graph, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (0, [start])) 

    # Set to keep track of visited nodes
    visited = set()

    while priority_queue:
        current_cost, path = heapq.heappop(priority_queue)
        current_node = path[-1]

        if current_node == goal:
            return path, current_cost

        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore neighbors
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                new_cost = current_cost + cost
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (new_cost, new_path))

    # If no path is found, return None
    return None, float('inf')

start_city = "Addis Ababa"
goal_city = "Lalibela"
path, total_cost = uniform_cost_search(state_space_graph, start_city, goal_city)

if path:
    print(f"Path from {start_city} to {goal_city}: {path}")
    print(f"Total cost: {total_cost}")
else:
    print(f"No path found from {start_city} to {goal_city}.")