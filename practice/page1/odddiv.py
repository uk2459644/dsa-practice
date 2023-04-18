import math

def fun(n):
    if n==1:
        return 1
    st=set()
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i%2==1:
                st.add(i)
            if (n//i)%2==1:
                st.add(n//i)
    return sum(st)

for _ in range(int(input())):
    l,r=map(int,input().split())
    ans=0
    lst=list()
    if l==r:
        ans=fun(l)
        print(ans)
    else:
        for a in range(l,r+1):
            nm=fun(a)
            ans+=nm
        print(ans)
