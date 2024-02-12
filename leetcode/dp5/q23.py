from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_bipartite_util(self,src,colorArr):
        colorArr[src]=1
        queue=[]
        queue.append(src)

        while queue:
            u=queue.pop(0)
            for v in self.graph[u]:
                if colorArr[v]==-1:
                    colorArr[v]=1-colorArr[u]
                    queue.append(v)
                elif colorArr[v]==colorArr[u]:
                    return False
        return True
    
    def is_bipartite(self):
        V=len(self.graph)
        colorArr=[-1]*V
        for i in range(V):
            if colorArr[i]==-1:
                if not self.is_bipartite_util(i,colorArr):
                    return False
        return True

