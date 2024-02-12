from collections import defaultdict

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

graph = defaultdict(list)

for u, v in prerequisites:
    graph[u].append(v)

paths = []
prelook=dict()

def dfs(node, path):
    prelook[node]=path
    path.append(node)
    if node not in graph:
        paths.append(path.copy())
    else:
        for v in graph[node]:
            dfs(v, path.copy())

    path.pop()

dfs(0, [])
print(prelook,graph)
