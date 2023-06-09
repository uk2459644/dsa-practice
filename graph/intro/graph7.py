from collections import defaultdict

class Graph:
    def __init__(self,vertices) -> None:
        self.graph=defaultdict(list)
        self.V=vertices
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self,v,visited,recStack):
        visited[v]=True
        recStack[v]=True

        for neighbour in self.graph[v]:
            if visited[neighbour]==False:
                if self.isCyclicUtil(neighbour,visited,recStack):
                    return True
                elif recStack[neighbour]==True:
                    return True
        recStack[v]=False
        return False
        