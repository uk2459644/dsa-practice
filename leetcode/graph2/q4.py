from collections import defaultdict,deque

n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

graph = defaultdict(list)

for i in range(n):
    graph[manager[i]].append(i)

queue=deque([(graph[-1][0],0)])

visited=set()
visited.add(graph[-1][0])

time=0
while queue:
    node,tm=queue.popleft()
    time=max(time,tm)
    for nod in graph[node]:
        if nod not in visited:
            queue.append((nod,time+informTime[node]))
            visited.add(nod)


print(time)




