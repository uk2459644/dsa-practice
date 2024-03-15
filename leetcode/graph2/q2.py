from collections import defaultdict

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]

graph = defaultdict(list)

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

def dfs(node,parent):
    ans=0
    for u in graph[node]:
        if u==parent:
            continue
        ans+=dfs(u,node)
    
    return ans+2 if ans or hasApple[node] else 0

res=dfs(0,-1)

print(res-2)

