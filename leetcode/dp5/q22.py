from collections import defaultdict,deque
import math

n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]

graph = defaultdict(list)

for a,b in redEdges:
    graph[a].append((b,'red'))

for a,b in blueEdges:
    graph[a].append((b,'blue'))

queue=deque([(0,"red",0),(0,"blue",0)])
visited=set()
ans=[math.inf]*n

while queue:
    node,color,level=queue.popleft()

    if (node,color) in visited:
        continue
    visited.add((node,color))
    ans[node]=min(ans[node],level)
    for v,c in graph[node]:
        if c!=color:
            queue.append((v,c,level+1))

dist=[-1 if x==math.inf else x for x in ans]

print(dist)




