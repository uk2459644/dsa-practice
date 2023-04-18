for _ in range(int(input())):
    n,k=map(int,input().split())
    klist=list(map(int,input().split()))
    klist.sort()
    pref=0
    ans=list()
    appendlist=list()
    for i in range(1,n+1):
        ans.append(i)
        if klist[pref]==i:
            ans.reverse()
            appendlist.append(ans)
            pref+=1 
            ans=[]
    
    appendlist.append(ans)
    prepperm=[]
    for lis in appendlist:
        prepperm+=lis
    print(*prepperm)