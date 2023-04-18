# An iterative python program to do DFS traversal from
# a given source vertex. DFS(int s ) traverses vertices
# reachable from s.

# this class represents a directed graph using adjacency
# list representation

class Graph:
    def __init__(self,V) -> None:
        self.V=V 
        self.adj=[[] for i in range(V)]

    def addEdge(self,v,w):
        self.adj[v].append(w)
    
    def DFS(self,s):
        visited=[False for i in range(self.V)]
        # create a stack for DFS
        stack=[]
        stack.append(s)
        while (len(stack)):
            s=stack[-1]
            stack.pop()

            if (not visited[s]):
                print(s,end=" ")
                visited[s]=True
            
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

# program for disconnected graph
class Graph:
    def __init__(self,V) -> None:
        self.V=V 
        self.adj=[[] for i in range(V)]
    
    def addEdge(self,v,w):
        self.adj[v].append(w)
    
    def DFSUtil(self,s,visited):
        stack=[]
        stack.append(s)
        while (len(stack)!=0):
            s=stack.pop()
            if (not visited[s]):
                print(s,end=" ")
                visited[s]=True
            i=0
            while i<len(self.adj[s]):
                if not visited[self.adj[s][i]]:
                    stack.append(self.adj[s][i])
                i+=1
    
    def DFS(self):
        visited=[False]*self.V
        for i in range(self.V):
            if not visited[i]:
                self.DFSUtil(i,visited)
                
