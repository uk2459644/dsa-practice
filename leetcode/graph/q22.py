from collections import defaultdict

parents = [-1,2,0]

n=len(parents)

graph=defaultdict(list)

for node,parent in enumerate(parents):
    graph[parent].append(node)

d=defaultdict(int)
def dfs(root):
    p,s=1,0
    for child in graph[root]:
        res=dfs(child)
        p*=res
        s+=res
    p*=max(1,n-s-1)
    d[p]+=1
    return s+1

dfs(0)

print(d[max(d.keys())])

