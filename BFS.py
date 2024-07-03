from collections import deque
from Graph_adjacencyList import Graph


class BFS:

    def __init__(self) -> None:
        self.g = Graph()
        self.g.addEdge(0, 1)
        self.g.addEdge(0, 2)
        self.g.addEdge(1, 2)
        self.g.addEdge(2, 0)
        self.g.addEdge(2, 3)
        self.g.addEdge(3, 3)
        self.q = deque()
        self.visited = set()
        self.output = []

    def traversal_iterative(self, starting_node):
        #add the node to the queue
        #visit the starting node
        self.q.append(starting_node)
        self.visited.add(starting_node)
        self.output.append(starting_node)
        """
        Visit all the neighbors first and then move to neighbor's of neighbor
        """
        while self.q:
            current = self.q.popleft()
            self.visited.add(current)            
            neighbors = self.g.graph[current]
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.output.append(neighbor)
                    self.q.append(neighbor)
                    self.visited.add(neighbor)
        return self.output



        
    


if __name__ == "__main__":
    traverse = BFS()
    print(traverse.traversal_iterative(1))