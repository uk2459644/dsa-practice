def f(n):
    sum=list()
    for i in range(1,n+1,2):
        m=n//i
        # sum+=(i*m)
        sum.append(m)
    # sum.sort()
    return sum

for i in range(int(input())):
    total=0
    l,r=map(int,input().split())
    # total=f(r)-f(l-1)
    print(f(r),f(l-1))