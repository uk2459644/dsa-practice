from collections import defaultdict

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]

graph=defaultdict(list)

vertex=set()

for i in range(n):
    vertex.add(i)

for i in range(n):
    if leftChild[i]!=-1:
        graph[i].append(leftChild[i])
        if leftChild[i] in vertex:
            vertex.remove(leftChild[i])
    
    if rightChild[i]!=-1:
        graph[i].append(rightChild[i])
        if rightChild[i] in vertex:
            vertex.remove(rightChild[i])

if len(vertex) != 1:
    print(False)

root=vertex.pop()
print(root)
visited=set()
def dfs(node):
    if node in visited:
        return False
    ans=True
    visited.add(node)
    for child in graph[node]:
        ans = ans and dfs(child)
    return ans

ans=dfs(root)

print(ans)


