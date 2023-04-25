for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    nli.sort()
    ans=0
    count=1
    for i in range(1,n):
        if nli[i]^nli[i-1]<=1:
            count+=1 
            # ans=max(ans,count)
        else:
            ans=max(ans,count)
            count=1
    
    ans=max(ans,count)
    print(n-ans)
