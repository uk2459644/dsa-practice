# program to print transitive closure of a graph

from collections import defaultdict

class Graph:
    def __init__(self,vertices) -> None:
        self.V=vertices
        self.graph=defaultdict(list)
        self.tc=[[0 for j in range(self.V)] for i in range(self.V)]

    def DFSUtil(self,s,v):
        if (s==v):
            if (v in self.graph[s]):
                self.tc[s][v]=1
        else:
            self.tc[s][v]=1
        
        for i in self.graph[v]:
            if self.tc[s][i]==0:
                if s==i:
                    self.tc[s][i]=1
                else:
                    self.DFSUtil(s,i)
    
    def transitiveClosure(self):
        for i in range(self.V):
            self.DFSUtil(i,i)
        print(self.tc)