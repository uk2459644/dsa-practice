from collections import defaultdict,deque

roads = [[1,13,14],[9,11,15],[2,11,11],[9,4,15],[3,11, 8]]

graph=defaultdict(dict)

for u,v,w in roads:
    graph[u][v]=graph[v][u]=w

ans=float('inf')
visited=set()
visited.add(1)

def dfs(source,ans):
    for neig,score in graph[source].items():
        ans=min(ans,score)
        min_dist=float('inf')
        if neig not in visited:
            visited.add(neig)
            min_dist=dfs(neig,score)
        ans=min(min_dist,ans)
    return ans



