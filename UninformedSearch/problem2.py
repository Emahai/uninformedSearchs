from collections import deque

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Pathfinding Function
def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    visited = set()
    if strategy == 'bfs':
        queue = deque([(start_city, [start_city], 0)])
        while queue:
            current_city, path, cost = queue.popleft()
            if current_city == goal_city:
                return path, cost
            if current_city not in visited:
                visited.add(current_city)
                for neighbor, distance in roads.get(current_city, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor], cost + distance))

    elif strategy == 'dfs':
        stack = [(start_city, [start_city], 0)]
        while stack:
            current_city, path, cost = stack.pop()
            if current_city == goal_city:
                return path, cost
            if current_city not in visited:
                visited.add(current_city)
                for neighbor, distance in roads.get(current_city, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor], cost + distance))

    return None, None

# Test Pathfinding
if __name__ == "__main__":
    start = 'Addis Ababa'
    goal = 'Mekelle'
    strategy = 'bfs'  # Change to 'dfs' for Depth-First Search
    path, cost = uninformed_path_finder(cities, roads, start, goal, strategy)
    print(f"Strategy: {strategy}")
    print(f"Path: {path}")
    print(f"Cost: {cost}")
