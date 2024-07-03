from Graph_adjacencyList import Graph
from collections import deque


class topsort:


    def __init__(self) -> None:
        self.g = Graph()
        self.g.addEdge(1,2)
        self.g.addEdge(1,3)
        self.g.addEdge(1,4)
        self.g.addEdge(2,3)
        self.g.addEdge(3,6)
        self.g.addEdge(4,5)
        self.g.addEdge(5,6)

        self.visited = set()
        
    def dfs(self, current, visitedNodes):
        neighbors = self.g.graph[current]
        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(neighbor, visitedNodes)
        visitedNodes.append(current)

    def get_top_ordering(self, start_node):
        output = [0] * (len(self.g.graph)+1)
        idx = len(self.g.graph)

        for i in range(1, 6):
            if i not in self.visited:
                visitedNodes = []
                self.dfs(i, visitedNodes)
                for node in visitedNodes:
                    output[idx] = node
                    idx -= 1
        return output
    

tp = topsort()
print(tp.get_top_ordering(1))   
