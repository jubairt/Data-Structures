class UiGraph:
    def __init__(self, edges=None) -> None:
        # Initialize the graph as a dictionary
        self.graph_dict = {}
        if edges:
            # Add edges from the provided list
            for start, end in edges:
                self.add_edge(start, end)

    def add_vertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, v, e):
        # Add an edge between two vertices (and ensure both vertices exist in the graph)
        if v not in self.graph_dict:
            self.add_vertex(v)
        if e not in self.graph_dict:
            self.add_vertex(e)
        self.graph_dict[v].append(e)
        self.graph_dict[e].append(v)

    def remove_vertex(self, v):
        # Remove a vertex and all edges associated with it
        if v in self.graph_dict:
            for e in self.graph_dict[v]:
                self.graph_dict[e].remove(v)
            del self.graph_dict[v]

    def remove_edge(self, v, e):
        # Remove an edge between two vertices
        if v in self.graph_dict and e in self.graph_dict[v]:
            self.graph_dict[v].remove(e)
            self.graph_dict[e].remove(v)

    def get_neighbours(self, v):
        # Return the neighbors of a vertex
        return self.graph_dict[v] if v in self.graph_dict else []

    def has_edge(self, v, e):
        # Check if an edge exists between two vertices
        return v in self.graph_dict and e in self.graph_dict[v]

    def find_paths(self, start, end, path=None):
        # Find all paths from start to end
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.graph_dict:
            return []
        path = path + [start]
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.find_paths(node, end, path)
                paths.extend(sp)
        return paths

    def shortest_path(self, start, end, path=None):
        # Find the shortest path from start to end
        if path is None:
            path = []
        if start == end:
            return path + [end]
        if start not in self.graph_dict:
            return []
        path = path + [start]
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path if shortest_path else []

    def bfs(self, start):
        # Perform Breadth-First Search from the start vertex
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node)
                queue.extend(self.graph_dict.get(node, []))
        return visited

    def dfs(self, start):
        # Perform Depth-First Search from the start vertex
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.graph_dict.get(node, []))
        return visited

    def __str__(self) -> str:
        # Return the string representation of the graph
        return str(self.graph_dict)


# Define your routes (edges) for the graph
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

# Create an instance of UiGraph with the routes
route_graph = UiGraph(routes)

# Test adding and removing vertices/edges
route_graph.add_vertex("Berlin")                # Adding a new vertex
route_graph.add_edge("Berlin", "New York")      # Adding an edge between Berlin and New York
route_graph.remove_edge("Paris", "Dubai")       # Removing the edge between Paris and Dubai

# Print the graph
print("Graph structure:", route_graph.graph_dict)

# Find all paths between Mumbai and New York
start, end = "Mumbai", "New York"
print(f"All paths between {start} and {end}: {route_graph.find_paths(start, end)}")

# Find the shortest path between Mumbai and New York
print(f"Shortest path between {start} and {end}: {route_graph.shortest_path(start, end)}")

# Perform BFS starting from Mumbai
print("BFS from Mumbai:")
route_graph.bfs("Mumbai")

# Perform DFS starting from Mumbai
print("\nDFS from Mumbai:")
route_graph.dfs("Mumbai")

# Output:
# Graph structure: {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Mumbai', 'New York'], 'Dubai': ['Mumbai', 'New York'], 'New York': ['Paris', 'Dubai', 'Toronto', 'Berlin'], 'Toronto': ['New York'], 'Berlin': ['New York']}
# All paths between Mumbai and New York: [['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]
# Shortest path between Mumbai and New York: ['Mumbai', 'Paris', 'New York']
# BFS from Mumbai:
# Mumbai
# Paris
# Dubai
# New York
# Toronto
# Berlin
#
# DFS from Mumbai:
# Mumbai
# Dubai
# New York
# Berlin
# Toronto
# Paris
