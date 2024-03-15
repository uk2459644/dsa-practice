from collections import defaultdict,deque


n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]


graph= defaultdict(list)

for i in range(n):
    graph[manager[i]].append(i)

lst=[0]*n
ans=0

queue=deque([headID])

while queue:
    node=queue.popleft()
    for nod in graph[node]:
        lst[nod]=(informTime[node]+lst[node])
        ans=max(ans,lst[nod])
        queue.append(nod)

print(ans)


