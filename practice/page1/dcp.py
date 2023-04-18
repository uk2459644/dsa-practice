mod=(10**9+7)
n,m=map(int,input().split())
nqli=list(map(int,input().split()))
nqli.insert(0,0)
for i in range(m):
    c,x=map(int,input().split())
    cq=nqli[c]
    if cq==0:
        continue
    nqli[c]=0
    cxli=list(map(int,input().split()))
    for j in range(0,2*x,2):
        uni=cxli[j]
        com=cxli[j+1]
        nqli[com]=((cq*uni)+nqli[com])%mod

del nqli[0]
print(*nqli,sep="\n")


