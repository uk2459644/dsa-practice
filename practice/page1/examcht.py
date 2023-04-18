import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(-1)
        continue
    diff=abs(a-b)
    fact=set()
    for i in range(1,int(math.sqrt(diff))+1):
        if diff%i==0:
            fact.add(i)
            fact.add(diff//i)
    print(len(fact))