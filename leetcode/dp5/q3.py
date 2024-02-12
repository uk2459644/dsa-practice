from collections import defaultdict,deque

roads = [[1,13,14],[9,11,15],[2,11,11],[9,4,15],[3,11, 8]]

graph = defaultdict(dict)

for u,v,w in roads:
    graph[u][v]=graph[v][u]=w

ans=10**5
visited=set()
queue=deque([1])

while queue:
    node=queue.popleft()
    visited.add(node)
    for v,d in graph[node].items():
        ans=min(ans,d)
        if v not in visited:
            queue.append(v)



print(graph,ans)


