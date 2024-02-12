from collections import defaultdict,deque

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

graph=defaultdict(list)

for u,v in prerequisites:
    graph[u].append(v)

def dfs(node,dest,visited:set):
    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            if v==dest:
                return True
            dfs(v,dest,visited)
    return False

nm=len(queries)
ans=[False]*nm
for i in range(nm):
    visited=set()
    if dfs(queries[i][0],queries[i][1],visited):
        ans[i]=True

print(ans,graph)



