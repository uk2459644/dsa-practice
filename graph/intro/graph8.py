# python program to check if a graph contains negative
# weight cycle using Bellman-Ford algorithm. This program
# works only if all vertices are reachable from a source vertex.

class Edge:
    def __init__(self) -> None:
        self.src=0
        self.dest=0
        self.weight=0

# a structure to represent a connected, directed and
# weighted graph
class Graph:
    def __init__(self) -> None:
        self.V=0 
        self.E=0
        self.edge=None

def createGraph(V,E):
    graph=Graph()
    graph.E=E
    graph.V=V
    graph.edge=[Edge() for i in range(graph.E)]
    return graph

def isNegCycleBellmanFord(graph,src):
    V=graph.V
    E=graph.E
    dist=[1000000 for i in range(V)]
    dist[src]=0
    for i in range(1,V):
        for j in range(E):
            u=graph.edge[i].src
            v=graph.edge[j].dest 
            weight=graph.edge[j].weight
            if (dist[u]!= 1000000 and dist[u]+weight < dist[v]):
                dist[v]=dist[u]+weight
        
        for i in range(E):
            u=graph.edge[i].src
            v=graph.edge[i].dest
            weight=graph.edge[i].weight
            if (dist[u]!=1000000 and dist[u]+weight < dist[v]):
                return True
        return False

# negative weight cycle using Floyd warshall Algorithm

V=4
INF=99999

def negCyclefloydWarshall(graph):
    # dist[][] will be the output matrix
    # that will finally have the shortest distances 
    # between every pair of vertices
    dist=[[0 for i in range(V+1)] for j in range(V+1)]
    # initialize the solution matrix same as input
    # graph matrix. or we can say the initital values
    # of shortest distances are based on paths considering 
    # no intermediate vertex.
    for i in range(V):
        for j in range(V):
            dist[i][j]=graph[i][j]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dist[i][k]+dist[k][j] < dist[i][j]):
                    dist[i][j]=dist[i][k]+dist[k][j]
    
    for i in range(V):
        if (dist[i][i]<0):
            return True
    
    return False
