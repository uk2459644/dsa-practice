from collections import defaultdict,deque

edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]

graph=defaultdict(list)

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited=set(restricted)

ans=0

def dfs(node):
    size=1
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            size+=dfs(neighbor)
    return size

ans=dfs(0)
print(visited,graph,ans)

