from collections import defaultdict

# this class represents a directed graph using adjacency
# list representation

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        # mark the current node as visited
        self.graph[u].append(v)
    
    def DFUtil(self,v,visited):
        # mark the current node visited
        # and print it
        visited.add(v)
        print(v,end=" ")
        # recur for all the vertices
        # adjacent to this vertices
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFUtil(neighbour,visited)
    # The function to do DFS traversal. It uses recursive
    # DFSutil()
    def DFS(self,v):
        visited=set()
        # call the recursive helper function to print
        # DFS traversal
        self.DFUtil(v,visited)

# Handling a disconnected graph
class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # a function used by DFS
    def DFSUtil(self,v,visited):
        # mark the current node as visited
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
    
    def DFS(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex,visited)
        
