
for _ in range(int(input())):
    n,m=map(int,input().split())
    i=n
    res1=n
    res2=n
    res=0
    while (i<=m and (m-i)>=res):
        a=i
        b=m-(m%i)
        if (abs(a-b)>res):
            res1=a
            res2=b
            res=abs(a-b)
        i+=1 
    
    print(res1,res2)