from collections import defaultdict,deque

n = 6 
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

nm=len(connections)

if nm<n-1:
    print(-1)
    

graph=defaultdict(list)

for u,v in connections:
    graph[u].append(v)
    graph[v].append(u)

visited=set()

count=0

def dfs(node):
    visited.add(node)

    for v in graph[node]:
        if v not in visited:
            visited.add(v)
            dfs(v)

for i in range(n):
    if i not in visited:
        dfs(i)
        count+=1

print(count)


