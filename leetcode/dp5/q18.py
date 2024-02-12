from collections import defaultdict,deque

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]

graph=defaultdict(list)

vertex=set()

for i in range(n):
    vertex.add(i)

for i in range(n):
    if rightChild[i]!=-1:
        graph[i].append(rightChild[i])
        if rightChild[i] in vertex:
            vertex.remove(rightChild[i])
    
    if leftChild[i]!=-1:
        graph[i].append(leftChild[i])
        if leftChild[i] in vertex:
            vertex.remove(leftChild[i])

root=vertex.pop()
visited=set()
queue=deque([root])
visited.add(root)
ans=True
while queue:
    node=queue.popleft()
    for child in graph[node]:
        if child in visited:
            ans=False
            break
        visited.add(child)
        queue.append(child)
        



