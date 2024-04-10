from collections import defaultdict

s = "pwqlmqm"
pairs = [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]]

n=len(s)
swaps=defaultdict(list)

for x,y in pairs:
    swaps[x].append(y)
    swaps[y].append(x)

def dfs(graph,node,visited:set,connected:list):
    if node not in visited:
        visited.add(node)
        connected.append(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited,connected)

visited=set()
connected_pairs=[]
for node in swaps:
    if node not in visited:
        connected=[]
        dfs(swaps,node,visited,connected)
        connected.sort()
        connected_pairs.append(connected)

ans=[ch for ch in s]
for prs in connected_pairs:
    chars=[]
    for i in prs:
        chars.append(s[i])
    
    chars.sort()
    ck=0
    for i in prs:
        ans[i]=chars[ck]
        ck+=1

res="".join(ans)
print(res)

