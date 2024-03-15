from collections import deque

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

n=len(graph)

colorArr=[-1]*n

def bfs(src):
    colorArr[src]=1
    queue=deque([src])
    while queue:
        node=queue.popleft()
        for v in graph[node]:
            if colorArr[v]==-1:
                colorArr[v]=1-colorArr[node]
                queue.append(v)
            elif colorArr[v]==colorArr[node]:
                return False
    return True

for i in range(n):
    if colorArr[i]==-1:
        if not bfs(i):
            return False

return True


