# program to find BFS traversal from a given source
# vertex. traverses vertices reachable from s

from collections import defaultdict
# this class represents a directed graph using 
# adjacency list representation

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # function to print a BFS of graph
    def BFS(self,s):
        # mark all the vertices as not visited
        visited=[False]*(max(self.graph)+1)
        queue=[]
        # mark the source node as visited and enque it
        queue.append(s)
        visited[s]=True
        while queue:
            # dequeue a vertex from 
            # queue and print it
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

# generic function for BFS traversal of a graph
# valid for directed as well as undirected graphs
# which can have multiple disconnected components

def bfsOfGraph(V,adj):
    bfs_traversal=[]
    vis=[False]*V
    for i in range(V):
        if (vis[i]==False):
            q=[]
            vis[i]=True
            q.append(i)
            while (len(q)>0):
                g_node=q.pop(0)
                bfs_traversal.append(g_node)
                for it in adj[g_node]:
                    if (vis[it]==False):
                        vis[it]=True
                        q.append(it)
    return bfs_traversal