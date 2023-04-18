# python program to check if a given
# directed graph is eulerian or not

from collections import defaultdict

class Grpah:
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = defaultdict(list)
        self.IN = [0]*vertices
    
    def addEdge(self,v,u):
        self.graph[v].append(u)
        self.IN[u]+=1 
    
    def DFSUtil(self,v,visited):
        visited[v]=True
        for node in self.graph[v]:
            if visited[node] == False:
                self.DFSUtil(node,visited)
    
    def getTranspose(self):
        gr=Grpah(self.V)
        for node in range(self.V):
            for child in self.graph[node]:
                gr.addEdge(child,node)
        return gr
    