# naive implementation of find

def find(parent,i):
    if (parent[i]==-1):
        return i
    return find(parent,parent[i])

# naive implementation of union
def union(parent,x,y):
    xset=find(parent,x)
    yset=find(parent,y)
    parent[xset]=yset

# a union by rank and path compression based
# program to detect cycle in a graph

from collections import defaultdict

class Graph:
    def __init__(self,num_of_v) -> None:
        self.num_of_v=num_of_v
        self.edges=defaultdict(list)
    # graph is represented as an array of edges
    def add_edge(self,u,v):
        self.edges[u].append(v)

class Subset:
    def __init__(self,parent,rank) -> None:
        self.parent=parent
        self.rank=rank

# a utitlity function to find set of an element
# node (use path compression technique)

def find(subset,node):
    if subset[node].parent !=node:
        subset[node].parent = find(subset,subset[node].parent)
    return subset[node].parent

def union(subsets,u,v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent=v
    else:
        subsets[v].parent=u
        subsets[u].rank+=1 

def isCycle(graph):
    subsets=[]
    for u in range(graph.num_of_v):
        subsets.append(Subset(u,0))
    
    for u in graph.edges:
        u_rep=find(subsets,u)
        for v in graph.edges[u]:
            v_rep=find(subsets,v)
            if u_rep == v_rep:
                return True
            else:
                union(subsets,u_rep,v_rep)