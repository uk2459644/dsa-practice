from collections import defaultdict,deque

n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]

red_graph=defaultdict(list)
blue_graph=defaultdict(list)

for a,b in redEdges:
    red_graph[a].append(b)

for u,v in blueEdges:
    blue_graph[u].append(v)

red_que=deque([0])
blue_que=deque([0])

red_dist=[-1]*n
blue_dist=[-1]*n

red_dist[0]=0
blue_dist[0]=0

while red_que or blue_que:
    if red_que:
        node=red_que.popleft()
        for v in blue_graph[node]:
            if blue_dist[v]==-1:
                blue_dist[v]=red_dist[v]+1
                blue_que.append(v)
    
    if blue_que:
        node=blue_que.popleft()
        for v in red_graph[node]:
            if red_dist[v]==-1:
                red_dist[v]=blue_dist[v]+1
                red_que.append(v)

ans=[0]*n
for i in range(n):
    if red_dist[i]==-1 or blue_dist[i]==-1:
        ans[i]=max(red_dist[i],blue_dist[i])
    else:
        ans[i]=min(red_dist[i],blue_dist[i])

print(ans)
