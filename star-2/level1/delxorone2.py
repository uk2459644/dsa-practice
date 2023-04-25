for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    set_nli=set(nli)
    ans=0

    for a in set_nli:
        count=nli.count(a)
        countx=0
        x=a^1
        if x in set_nli:
            countx=nli.count(x)
        
        ans=max(ans,count+countx)
    
    print(n-ans)