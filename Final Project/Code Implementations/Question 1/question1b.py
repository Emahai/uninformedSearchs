from collections import deque  
from question1a import state_space_graph

class TravelingEthiopiaSolver:
    def __init__(self, graph):
        self.graph = graph  

    def bfs(self, start, goal):
        """
        Breadth-First Search (BFS) implementation.
        """
        queue = deque() 
        queue.append([start])  

        while queue:
            path = queue.popleft() 
            current_city = path[-1] 

            if current_city == goal:
                return path  

            # Explore all connected cities
            for neighbor in self.graph.get(current_city, []):
                if neighbor not in path:  
                    new_path = list(path) 
                    new_path.append(neighbor) 
                    queue.append(new_path)  

        return None 

    def dfs(self, start, goal):
        """
        Depth-First Search (DFS) implementation.
        """
        stack = deque()  
        stack.append([start]) 

        while stack:
            path = stack.pop()  
            current_city = path[-1]  

            if current_city == goal:
                return path  

            # Explore all connected cities
            for neighbor in self.graph.get(current_city, []):
                if neighbor not in path: 
                    new_path = list(path) 
                    new_path.append(neighbor)  
                    stack.append(new_path) 

        return None  

    def solve(self, start, goal, strategy):
        """
        Solves the problem using the given strategy (BFS or DFS).
        """
        if strategy == "BFS":
            return self.bfs(start, goal)
        elif strategy == "DFS":
            return self.dfs(start, goal)
        else:
            raise ValueError("Invalid strategy. Use 'BFS' or 'DFS'.")
        

# Create an instance 
solver = TravelingEthiopiaSolver(state_space_graph)

# Solve using BFS
start_city = "Addis Ababa"
goal_city = "Babile"
bfs_path = solver.solve(start_city, goal_city, "BFS")
print("BFS Path:", bfs_path)

# Solve using DFS
dfs_path = solver.solve(start_city, goal_city, "DFS")
print("DFS Path:", dfs_path)