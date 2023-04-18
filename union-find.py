def find(node,par):
    res=node
    while res!=par[res]:
        par[res]=par[par[res]]
        res=par[res]
    return res

def union(a,b,par,rank):
    p1,p2=find(a,par),find(b,par)
    if p1==p2:
        return 0
    if rank[p2]>rank[p1]:
        par[p1]=p2
        rank[p2]+=rank[p1]
    else:
        par[p2]=p1
        rank[p1]+=rank[p2]
    
    return 1

for _ in range(int(input())):
    n,m=map(int,input().split())
    par=[i for i in range(n)]
    rank=[1 for i in range(n)]
    for j in range(m):
        a,b=map(int,input().split())
        union(a,b,par,rank)
    for i in range(int(input())):
        x,y=map(int,input().split())
        if find(x,par)==find(y,par):
            print('YO')
        else:
            print('NO')