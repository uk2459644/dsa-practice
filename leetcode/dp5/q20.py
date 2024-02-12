from collections import defaultdict,deque

n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]

graph=defaultdict(list)

for u,v in redEdges:
    graph[u].append(v)

for u,v in blueEdges:
    graph[u].append(v)

ans=[10**9]*n
ans[0]=0
visited=set()
visited.add(0)

queue=deque([0])
colors=[""]*n
colors[0]="rb"

level=0
while queue:
    for _ in range(len(queue)):
        node=queue.popleft()
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
                nc=colors[node]
                if nc=="rb":
                    if [node,child] in redEdges and [node,child] in blueEdges:
                        colors[child]="rb"
                        ans[child]=min(ans[child],level+1)
                    elif [node,child] in redEdges:
                        colors[child]="r"
                        ans[child]=min(ans[child],level+1)
                    elif [node,child] in blueEdges:
                        colors[child]="b"
                        ans[child]=min(ans[child],level+1)
                elif nc=="b":
                    if [node,child] in redEdges:
                        colors[child]="r"
                        ans[child]=min(ans[child],level+1)
                elif nc=="r":
                    if [node,child] in blueEdges:
                        colors[child]="b"
                        ans[child]=min(ans[child],level+1)
    level+=1
for i in range(n):
    if ans[i]==10**9:
        ans[i]=-1
print(ans,graph)




