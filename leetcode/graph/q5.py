
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        
        return self.parent[u]
    
    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)

        if root_u==root_v:
            return False
        
        if self.rank[root_u]<self.rank[root_v]:
            self.parent[root_u]=root_v
        elif self.rank[root_u]>self.rank[root_v]:
            self.parent[root_v]=root_u
        else:
            self.parent[root_v]=root_u
            self.rank[root_u]+=1
        
        return True

def kruskal(graph):
    edges = sorted(graph,key=lambda x:x[2])
    n=len(edges)

    # Initialize Disjoint Set
    ds=DisjointSet(n)

    # Initialize MST
    MST=[]

    for edge in edges:
        u,v,weight=edge
        if ds.union(u,v):
            MST.append(edge)
    
    return MST


