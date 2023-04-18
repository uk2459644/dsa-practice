# python program for union - find algorithm
# to detect cycle in a undirected graph
# we have one edge for any two vertex

from collections import defaultdict

class Graph:
    def __init__(self,vertices) -> None:
        self.V=vertices
        self.graph=defaultdict(list)
    
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # a utility function to find the subset of an element
    def find_parent(self,parent,i):
        if parent[i]==i:
            return i
        if parent[i]!=i:
            return self.find_parent(parent,parent[i])
    
    # a utility function to do union of two subsets
    def union(self,parent,x,y):
        parent[x]=y
    
    def isCycle(self):
        # allocate memory for creating V subsets and
        # initialize all subsets as single element sets
        parent=[0]*(self.V)
        for i in range(self.V):
            parent[i]=i
        
        for i in self.graph:
            for j in self.graph:
                x=self.find_parent(parent,i)
                y=self.find_parent(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)
                
