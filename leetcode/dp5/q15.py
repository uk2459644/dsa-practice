from collections import defaultdict,deque

numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]

graph = defaultdict(list)

for u,v in prerequisites:
    graph[u].append(v)

paths=list()

def dfs(node,path:list):
    if node not in graph:
        path.append(node)
        paths.append(path)
        return
    path.append(node)
    for v in graph[node]:
        dfs(v,path.copy())
        dfs(v,[])

dfs(0,[])

print(paths)

    

