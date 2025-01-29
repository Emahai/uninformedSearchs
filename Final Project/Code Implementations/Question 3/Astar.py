from dictionary import state_space_graph_cost,state_space_graph_heuristic
import heapq

class AStarSearch:
    def __init__(self, graph_cost, graph_heuristic):
        self.graph_cost = graph_cost  
        self.graph_heuristic = graph_heuristic 

    def astar_search(self, start, goal):
        priority_queue = []
        heapq.heappush(priority_queue, (0, 0, [start])) 

        # Set to keep track of visited nodes
        visited = set()

        while priority_queue:
            total_cost, path_cost, path = heapq.heappop(priority_queue)
            current_city = path[-1]

            if current_city == goal:
                return path, path_cost

            if current_city in visited:
                continue

            # Mark the city as visited
            visited.add(current_city)

            # Explore neighbors
            for neighbor, cost in self.graph_cost.get(current_city, []):
                if neighbor not in visited:
                    new_path_cost = path_cost + cost
                    total_cost = new_path_cost + self.graph_heuristic.get(neighbor, 0)
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(priority_queue, (total_cost, new_path_cost, new_path))

        return None, float('inf')
    
# Create an instance 
astar = AStarSearch(state_space_graph_cost, state_space_graph_heuristic)

# Perform A* search from Addis Ababa to Moyale
start_city = "Addis Ababa"
goal_city = "Moyale"
path, total_cost = astar.astar_search(start_city, goal_city)

# Output the result
if path:
    print(f"Optimal path from {start_city} to {goal_city}: {path}")
    print(f"Total cost: {total_cost}")
else:
    print(f"No path found from {start_city} to {goal_city}.")