from collections import deque

rooms = [[1,3],[3,0,1],[2],[0]]

visited=set()

queue=deque([0])

while queue:
    u=queue.popleft()
    visited.add(u)
    for v in rooms[u]:
        if v not in visited:
            queue.append(v)

if len(visited)==len(rooms):
    return True
else:
    return False

