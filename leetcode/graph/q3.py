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
    
    # Function to find the vertex with the minimum distance value,
    # from the set of vertices not yet included in the shortest path tree

    def min_distance(self,dist,visited):
        min_dist = sys.maxsize
        min_index = None
        
    



