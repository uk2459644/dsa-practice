from collections import defaultdict,deque

graph = [[1,2],[2,3],[5],[0],[5],[],[]]

dGraph=defaultdict(list)
n=len(graph)
indegree=[0]*n
for i in range(n):
    c=0
    for nm in graph[i]:
        c+=1
        dGraph[nm].append(i)
    indegree[i]+=c

queue=deque()
for i in range(n):
    if indegree[i]==0:
        queue.append(i)

visited=set()

while queue:
    u=queue.popleft()
    visited.add(u)
    for v in dGraph[u]:
        if v not in visited:
            # visited.add(v)
            indegree[v]-=1
            if indegree[v]==0:
                queue.append(v)

# print(dGraph,indegree,visited)
ans=list(visited)
ans.sort()
print(ans)




