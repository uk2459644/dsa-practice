from collections import defaultdict,deque

edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
n = 7
graph = defaultdict(list)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = set()


def bfs(node):
    count=0
    queue=deque([node])
    visited.add(node)
    while queue:
        nd=queue.popleft()
        count+=1
        for vtx in graph[nd]:
            if vtx not in visited:
                visited.add(vtx)
                queue.append(vtx)
    return count


component_sizes = []

for i in range(n):
    if i not in visited:
        size = bfs(i)
        component_sizes.append(size)

print(component_sizes)
