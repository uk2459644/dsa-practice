from collections import defaultdict

class Graph:
    # constructor
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor,visited)
    
    def DFS(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex,visited)

if __name__=="__main__":
    print("Following is Depth First Traversal \n")
    g=Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    g.DFS()
    