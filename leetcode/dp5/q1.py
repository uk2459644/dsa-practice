from collections import defaultdict,deque

roads = [[1,13,14],[9,11,15],[2,11,11],[9,4,15],[3,11, 8]]

graph=defaultdict(list)
dgraph=defaultdict(int)
n=13
for r in roads:
    graph[r[0]].append(r[1])
    graph[r[1]].append(r[0])

    dgraph[str(r[0])+">"+str(r[1])]=r[2]
    dgraph[str(r[1])+">"+str(r[0])]=r[2]

queue=deque()
queue.append(1)
visited=[False]*(n+1)
ans_min=10**5
while queue:
    curr_len=len(queue)
    for _ in range(curr_len): 
        vtx=queue.popleft()
        visited[vtx]=True
        for v in graph[vtx]:
            if vtx>1:
                d1=dgraph[str(v)+">"+str(vtx)]
                ans_min=min(d1,ans_min)
            if not visited[v]:
                queue.append(v)
                visited[v]=True

print(ans_min,dgraph)

    



