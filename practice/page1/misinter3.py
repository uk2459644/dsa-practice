import sys
input=sys.stdin.readline

def inp():
    return int(input())

mod=(10**9)+7

for _ in range(inp()):
    n=inp()
    eli=list()
    oli=list()
    for i in range(1,n+1):
        if i%2==0:
            eli.append(i)
        else:
            oli.append(i)
    nli=eli+oli
    vis=[False]*(n+1)
    count=0
    for j in range(1,n+1):
        if vis[j]==False:
            count+=1
            temp=nli[j]
            while vis[temp]==False:
                vis[temp]=True
                temp=nli[temp]
    print(pow(26,count,mod))
