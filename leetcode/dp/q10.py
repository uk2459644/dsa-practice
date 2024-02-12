
import sys

nli=list(map(int,input().split()))
n=len(nli)

dp=[-1 for i in range(n)]

def solve(arr,pos,n,c):
    if pos>=n-1:
        dp[-1]=0
        return c
    
    if dp[pos]!=-1:
        return dp[pos]+c
    
    mini=sys.maxsize
    for i in range(1,arr[pos]+1):
        if pos+i>=n:
            break
        mini=min(solve(arr,pos+i,n,1),mini)
    
    dp[pos]=mini
    return mini+c






