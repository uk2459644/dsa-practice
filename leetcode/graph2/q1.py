from collections import defaultdict

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]

graph = defaultdict(list)

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

def dfs(u,p):
    res = (hasApple[u], 0)
    for v in graph[u]:
        if v == p: continue
        apple, cost = dfs(v, u)
        if apple: res = (True, res[1] + cost + 2)
    
    return res
    
res=dfs(0,-1)

print(res)

