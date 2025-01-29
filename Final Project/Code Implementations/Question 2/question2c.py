from question2b import uniform_cost_search
from question2a import state_space_graph

def customized_uniform_cost_search(graph, start, goals):

    remaining_goals = set(goals)  
    current_city = start 
    total_path = [start] 
    total_cost = 0  

    while remaining_goals:
        best_path = None
        best_cost = float('inf')
        best_goal = None

        for goal in remaining_goals:
            path, cost = uniform_cost_search(graph, current_city, goal)
            if cost < best_cost:
                best_cost = cost
                best_path = path
                best_goal = goal

        if not best_path:
            break

        total_path.extend(best_path[1:])  
        total_cost += best_cost

        current_city = best_goal
        remaining_goals.remove(best_goal)

    return total_path, total_cost

start_city = "Addis Ababa"
goal_cities = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]
path, total_cost = customized_uniform_cost_search(state_space_graph, start_city, goal_cities)

if path:
    print(f"Path to visit all goal cities: {path}")
    print(f"Total cost: {total_cost}")
else:
    print("No path found to visit all goal cities.")