from Graph_adjacencyList import Graph

class DFS:
    
    visited = set()

    def __init__(self) -> None:
        self.g = Graph()
        self.g.addEdge(0, 1)
        self.g.addEdge(0, 2)
        self.g.addEdge(1, 2)
        self.g.addEdge(2, 0)
        self.g.addEdge(2, 3)
        self.g.addEdge(3, 3)

    def traversal_recursion(self, current, output):
        self.visited.add(current)
        output.append(current)
        neighbors = self.g.graph[current]
        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.traversal_recursion(neighbor, output)
        




traverse = DFS()
output = []
traverse.traversal_recursion(2, output)
print(output)    