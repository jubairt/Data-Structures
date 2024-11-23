class Digraph:
    def __init__(self, edges=None) -> None:
        # Initialize the graph as a dictionary
        self.dict = {}
        if edges:
            for start, end in edges:
                self.add_edge(start, end)

    def add_edge(self, vertex, edge):
        # Add an edge from vertex to edge
        if vertex in self.dict:
            self.dict[vertex].append(edge)
        else:
            self.dict[vertex] = [edge]

    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't already exist
        if vertex not in self.dict:
            self.dict[vertex] = []

    def remove_vertex(self, vertex):
        # Remove the vertex and all edges pointing to it
        if vertex in self.dict:
            for v in self.dict:
                if vertex in self.dict[v]:
                    self.dict[v].remove(vertex)  # Remove edge pointing to the vertex
            del self.dict[vertex]

    def remove_edge(self, vertex, edge):
        # Remove a specific edge from the graph
        if vertex in self.dict and edge in self.dict[vertex]:
            self.dict[vertex].remove(edge)

    def find_paths(self, start, end, path=None):
        # Recursively find all paths between start and end nodes
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.dict:
            return []
        path = path + [start]
        paths = []
        for node in self.dict[start]:
            if node not in path:
                sp = self.find_paths(node, end, path)
                paths.extend(sp)
        return paths

    def shortest_path(self, start, end, path=None):
        # Recursively find the shortest path between start and end nodes
        if path is None:
            path = []
        if start == end:
            return path + [end]
        if start not in self.dict:
            return None
        path = path + [start]
        shortest_path = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    def bfs(self, start):
        # Perform Breadth-First Search (BFS) starting from a given node
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                queue.extend(self.dict.get(node, []))
        return visited

    def dfs(self, start):
        # Perform Depth-First Search (DFS) starting from a given node
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.dict.get(node, []))
        return visited

    def __str__(self) -> str:
        # Return the string representation of the graph
        return str(self.dict)


if __name__ == '__main__':
    # Define routes as edges for the directed graph
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    # Create the directed graph
    route_graph = Digraph(routes)

    # Test adding and removing vertices/edges
    route_graph.add_vertex("Berlin")
    route_graph.add_edge("Berlin", "New York")
    route_graph.remove_edge("Paris", "Dubai")

    print(route_graph)

    # Find paths and shortest paths
    start, end = "Mumbai", "New York"
    print(f"All paths between {start} and {end}: {route_graph.find_paths(start, end)}")
    print(f"Shortest path between {start} and {end}: {route_graph.shortest_path(start, end)}")

    # BFS and DFS traversal
    print("BFS from Mumbai:")
    route_graph.bfs("Mumbai")

    print("\nDFS from Mumbai:")
    route_graph.dfs("Mumbai")

# Output:
# {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['New York'], 'Dubai': ['New York'], 'New York': ['Toronto'], 'Berlin': ['New York']}
# All paths between Mumbai and New York: [['Mumbai', 'Paris', 'New York'], ['Mumbai', 'Dubai', 'New York']]
# Shortest path between Mumbai and New York: ['Mumbai', 'Paris', 'New York']
# BFS from Mumbai:
# Mumbai
# Paris
# Dubai
# New York
# Toronto
#
# DFS from Mumbai:
# Mumbai
# Dubai
# New York
# Toronto
# Paris
