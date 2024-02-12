from collections import defaultdict
import math

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]

graph=defaultdict(list)

for a,b in roads:
    graph[a].append(b)
    graph[b].append(a)
ans=0
seat=4
def dfs(node,parent):
    # nonlocal ans
    size=1
    for neighbor in graph[node]:
        if neighbor==parent:
            continue
        size+=dfs(neighbor,node)
    if node!=0:
        ans+=math.ceil(size/seat)
    
    return size




print(graph)


