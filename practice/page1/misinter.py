import sys
input=sys.stdin.readline

def inp():
    return (int(input()))

def inlt():
    return list(map(int,input().split()))
def insr():
    s=input()
    return (list(s[:len(s)-1]))

mod=(10**9)+7
def solve(num):
    while num!=0:
        temp=nli[num-1]
        nli[num-1]=0
        num=temp

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
    count=0
    
    for i in range(n):
        if nli[i]!=0:
            count+=1
            solve(nli[i])
    ans=pow(26,count,mod)
    print(ans)
