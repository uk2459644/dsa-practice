import math 

for _ in range(int(input())):
    n=int(input())
    a_li=list(map(int,input().split()))
    a_li.sort()
    ans=0
    mid=int(math.floor(n/2))
    mid_value = a_li[mid]
    for i in range(n):
        if a_li[i]>=mid_value:
            ans+=1
    
    print(ans)