from collections import deque

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Traversal Function
def traverse_all_cities(cities, roads, start_city, strategy):
    def dfs(current_city, visited, path, cost):
        visited.add(current_city)
        path.append(current_city)
        all_paths.append((list(path), cost))  

        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                dfs(neighbor, visited, path, cost + distance)

        visited.remove(current_city)
        path.pop()

    def bfs():
        queue = deque([(start_city, [start_city], 0)])  
        while queue:
            current_city, path, cost = queue.popleft()
            all_paths.append((path, cost))  
            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in path:  
                    queue.append((neighbor, path + [neighbor], cost + distance))

    all_paths = []
    if strategy == 'dfs':
        dfs(start_city, set(), [], 0)
    elif strategy == 'bfs':
        bfs()

    best_path, best_cost = max(all_paths, key=lambda x: (len(x[0]), -x[1]))
    return best_path, best_cost

# Test Traversal
if __name__ == "__main__":
    start = 'Addis Ababa'
    strategy = 'dfs'  # Change to 'bfs' for Breadth-First Search
    path, cost = traverse_all_cities(cities, roads, start, strategy)
    print(f"Strategy: {strategy}")
    print(f"Path: {path}")
    print(f"Cost: {cost}")
