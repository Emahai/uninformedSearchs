from dictionary import city_neighbours, terminal_nodes

class MiniMax:
    def __init__(self, city_neighbours, terminal_nodes, initial_city="Addis Ababa"):
        self.city_neighbours = city_neighbours
        self.terminal_nodes = terminal_nodes
        self.initial_city = initial_city

    def minimax(self, current_city, depth, is_maximizing, visited):
        print(f"Current City: {current_city}, Depth: {depth}, Maximizing: {is_maximizing}")

        if current_city in self.terminal_nodes:
            print(f"Terminal Node: {current_city}, Value: {self.terminal_nodes[current_city]}")
            return self.terminal_nodes[current_city]

        if depth == 0:
            print(f"Depth Exhausted: {current_city}, Value: 0")
            return 0

        visited.add(current_city)

        if is_maximizing:
            max_eval = float('-inf')
            for neighbour in self.city_neighbours[current_city]:
                if neighbour not in visited:  
                    eval = self.minimax(neighbour, depth - 1, False, visited.copy())
                    max_eval = max(max_eval, eval)
            print(f"Maximizing: {current_city}, Best Value: {max_eval}")
            return max_eval
        else:
            min_eval = float('inf')
            for neighbour in self.city_neighbours[current_city]:
                if neighbour not in visited:  
                    eval = self.minimax(neighbour, depth - 1, True, visited.copy())
                    min_eval = min(min_eval, eval)
            print(f"Minimizing: {current_city}, Best Value: {min_eval}")
            return min_eval

    def find_best_move(self, depth):
        best_move = None
        best_value = float('-inf')
        for neighbour in self.city_neighbours[self.initial_city]:
            print(f"Evaluating Move: {neighbour}")
            visited = set()  
            move_value = self.minimax(neighbour, depth - 1, False, visited)
            print(f"Move: {neighbour}, Value: {move_value}")
            if move_value > best_value:
                best_value = move_value
                best_move = neighbour
        return best_move, best_value


# Initialize
mini_max_search = MiniMax(city_neighbours, terminal_nodes)

# Find the best move for the agent with a depth of 16
best_move, best_value = mini_max_search.find_best_move(depth=16)
print(f"Best move: {best_move}, Best value: {best_value}")