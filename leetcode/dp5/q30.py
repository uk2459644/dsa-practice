from collections import defaultdict,deque

times = [[1,2,1],[2,1,3]]
n=2
k=2

graph=defaultdict(list)

for u,v,w in times:
    graph[u].append((v,w))

ans=-1
queue=deque([(k,0)])
visited=set()
visited.add(k)
while queue:
    node,time=queue.popleft()
    if node in graph:
        for v,t in graph[node]:
            if v not in visited:
                visited.add(v)
                tm=t+time
                ans=max(ans,tm)
                queue.append((v,tm))

if len(visited)==n:
    print(ans)
else:
    print(-1)

