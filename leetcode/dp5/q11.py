from collections import defaultdict,deque

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

graph=defaultdict(list)
dummy=defaultdict(list)

for u,v in connections:
    dummy[u].append(v)
    graph[u].append(v)
    graph[v].append(u)

visited=set()
def dfs(parent,node,count):
    if parent!=-1:
        ls=dummy[parent]
        if node in ls:
            count+=1
    visited.add(node)
    for vtx in graph[node]:
        if vtx not in visited:
           count=dfs(node,vtx,count)
    # count+=1
    return count

print(dfs(-1,0,0))
print(dummy,graph)



