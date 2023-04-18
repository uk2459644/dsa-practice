for _ in range(int(input())):
    n,d=map(int,input().split())
    nli=list(map(int,input().split()))
    nli.sort(reverse=True)
    lst=list()
    ind=0
    while ind < (n-1):
        if (nli[ind]-nli[ind+1])<d:
            lst.append(nli[ind+1])
            lst.append(nli[ind])
            ind+=2
        else:
            ind+=1
    print(sum(lst))

   