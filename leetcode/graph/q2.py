import sys

class Graph:
    def __init__(self):
        self.graph={}
    
    # Function to add an edge to the graph
    def add_edge(self,u,v,weight):
        if u not in self.graph:
            self.graph[u]={}
        if v not in self.graph:
            self.graph[v]={}
        
        self.graph[u][v]=weight
        self.graph[v][u]=weight
    
    # A utility function to find the vertex with the minimum
    # key value, from the set of vertices not yet included in
    # the MST
    def minKey(self,key,mstSet):
        min_val=sys.maxsize
        min_inndex=-1

        for v in range(len(key)):
            if key[v]<min_val and not mstSet[v]:
                min_val=key[v]
                min_inndex=v
        
        return min_inndex
    
    # Function to construct and print MST for a graph
    # represented using adjacency list representation
    def primMST(self):
        # Key values used to pick minimum weight edge in cut
        key=[sys.maxsize]*len(self.graph)
        parent=[None]*len(self.graph)
        key[0]=0
        mstSet=[False]*len(self.graph)
        parent[0]=-1

        for _ in range(len(self.graph)):
            u=self.minKey(key,mstSet)
            mstSet[u]=True

            for v in self.graph[u]:
                if not mstSet[v] and self.graph[u][v] < key[v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
                    

