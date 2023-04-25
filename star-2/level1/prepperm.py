for _ in range(int(input())):
    n,k=map(int,input().split())
    klist=list(map(int,input().split()))
    klist.sort()
    nli=list(range(1,n+1))
    prep=0
    for a in klist:
        ali=nli[prep:a]
        ali.sort(reverse=True)
        nli=nli[:prep]+ali+nli[a:]
        prep=a
    
    print(*nli)