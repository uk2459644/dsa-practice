# python program to detect cycle in an undirected graph

from collections import defaultdict

# this class represents a undirected graph 
# using adjacency list representation

class Graph:
    def __init__(self,vertices) -> None:
        self.V=vertices
        self.graph=defaultdict(list)
    
    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    def isCycleUtil(self,v,visited,parent):
        visited[v]=True
        for i in self.graph[v]:
            if (self.isCycleUtil(i,visited,v)):
                return True
            elif parent!=i:
                return True
        return False
    
    def isCycle(self):
        visited=[False]*(self.V)

        for i in range(self.V):
            if visited[i]==False:
                if (self.isCycleUtil(i,visited,-1))==True:
                    return True
        
        return False
        