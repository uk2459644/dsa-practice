from collections import defaultdict
# this class represents a undirected graph
# using adjacency list representation

class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    # a recursive function that uses visited[]
    # and parent to detect cycle in subgraph reachable from verrtex v.

    def isCyclicUtil(self,v,visited, parent):
        # mark the current node as visited
        visited[v]=True
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                if (self.isCyclicUtil(i,visited,v)):
                    return True
            # if an adjacent vertex is visited and
            # not parent of current vertex, then
            # there is a cycle
            elif parent!=i:
                return True
        return False
    
    def isCycle(self):
        # mark all the vertices as not visited
        visited = [False]*(self.V)
        # call the recursive helper
        # function to detect cycle in different 
        # DFS trees
        for i in range(self.V):
            # don't recur if it is already visited
            if visited[i] == False:
                if (self.isCyclicUtil(i,visited,-1))==True:
                    return True
        return False

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.isCycle():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
 
 
if g1.isCycle():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
 