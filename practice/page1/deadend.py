for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    nli.sort()
    nli.insert(0,-5)
    nli.append(-5)
    cnt=0
    for i in range(1,n+1):
        if (nli[i]+1)!=nli[i+1] and nli[i]!=(nli[i-1]+1):
            cnt+=1
            nli[i]+=1
    print(cnt)