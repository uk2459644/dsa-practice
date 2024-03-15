from collections import defaultdict,deque

n = 4
dislikes = [[1,2],[1,3],[2,4]]

graph=defaultdict(list)

for a,b in dislikes:
    graph[a].append(b)
    graph[b].append(a)

colorArr=[-1]*(n+1)

def bfs(src):
    queue=deque([src])
    colorArr[src]=1
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if colorArr[v]==-1:
                colorArr[v]=1-colorArr[u]
                queue.append(v)
            elif colorArr[v]==colorArr[u]:
                return False
    return True

for i in range(1,n+1):
    if colorArr[i]==-1:
        if not bfs(i):
            return False

return True


