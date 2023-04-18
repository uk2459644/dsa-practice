def find(parent,node):
    if (node==parent[node]):
        return node
    parent[node]=find(parent,parent[node])
    return parent[node]

for _ in range(int(input())):
    n,m=map(int,input().split())
    parent=[i for i in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        up=find(parent,u)
        vp=find(parent,v)
        mn=min(up,vp)
        parent[u]=mn
        parent[v]=mn
    q=int(input())
    for j in range(q):
        a,b=map(int,input().split())
        if (find(parent,a)==find(parent,b)):
            print('YO')
        else:
            print('NO')
