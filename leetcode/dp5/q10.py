from collections import defaultdict,deque

edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
n=8
graph=defaultdict(list)

for u,v in edgeList:
    graph[v].append(u)

def bfs(node):
    ans=[]
    queue=deque([node])
    visited=set()
    while queue:
        vtx=queue.popleft()
        visited.add(vtx)
        ans.append(vtx)
        for v in graph[vtx]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    del ans[0]
    ans.sort()
    return ans
ans_li=[]
for i in range(n):
    an=bfs(i)
    ans_li.append(an)

print(ans_li)



