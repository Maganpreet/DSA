from collections import defaultdict

class Graph:


    def __init__(self) -> None:
        self.graph = defaultdict(list)


    #using adjacency list
    def addEdge(self,u,v):
        self.graph[u].append(v)


__package__ = 'Graph'
print(__package__, __name__)

 