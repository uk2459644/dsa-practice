from collections import deque

graph=[[4,3,1],[3,2,4],[3],[4],[]]
paths=[]
queue=deque([(0,[0])])

while queue:
    node,path=queue.popleft()
    if node==n-1:
        paths.append(path)
    else:
        for vtx in graph[node]:
            queue.append((vtx,path+[vtx]))

return paths

