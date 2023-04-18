for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[1]*(n+1)
    k=0
    for i in range(2,n+1):
        a=m%i
        k+=l[a]
        for j in range(a,n,i):
            l[j]+=1 
    print(k)