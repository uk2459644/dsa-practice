for _ in range(int(input())):
    n,k,l=map(int,input().split())
    result=0
    if (k+l)>=n:
        dif=abs(n-k-l)
        k=k-dif
        l=l-dif
        result=k*l
    else:
        m=n-k-l
        msm=(m*(m-1))//2
        result=(k*m+k*l+m*l+msm)
    print(result)