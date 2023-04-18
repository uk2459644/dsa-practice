
mod=10**9+7 

for _ in range(int(input())):
    n=int(input())
    freq=[0]*(n+1)
    for x in map(int,input().split()):
        if x<=n:
            freq[x]+=1 
    
    cur,ans=1,0 
    for i in range(1,n+1):
        cur=(cur*freq[i])%mod
        ans+=cur 
    print(ans%mod)
    