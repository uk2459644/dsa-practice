"""\
    Let's say we have c elements having p-th bit on.
    In one operation, we
    can turn K of them off. So by basic math, we can see that we
    need at least ceil(c/k) operations.
"""
import math 

for _ in range(int(input())):
    n,k=map(int,input().split())
    ali=list(map(int,input().split()))
    set_li=[0]*32
    for a in ali:
        for x in range(0,32):
            if a&(1<<x)>0:
                set_li[x]+=1
    
    ans=0
    for c in set_li:
        ans+=math.ceil(c/k)

