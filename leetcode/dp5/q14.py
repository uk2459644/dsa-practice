from collections import defaultdict,deque

numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]

graph = defaultdict(list)
indegree=defaultdict(int)

for u,v in prerequisites:
    graph[u].append(v)
    indegree[v]+=1

queue=deque()
for i in range(numCourses):
    if indegree[i]==0:
        queue.append(i)

prelook=defaultdict(set)
while queue:
    vtx=queue.popleft()
    for v in graph[vtx]:
        indegree[v]-=1
        prelook[v].add(vtx)
        prelook[v].update(prelook[vtx])
        if indegree[v]==0:
            queue.append(v)

ans=list()
for v1,v2 in queries:
    if v1 in prelook[v2]:
        ans.append(True)
    else:
        ans.append(False)

print(prelook,ans)

