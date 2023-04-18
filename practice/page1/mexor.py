import math
for _ in range(int(input())):
    x=int(input())
    if x==0:
        print(1)
    elif x==1 or x==2:
        print(2)
    else:
        y=int(math.log2(x+1))
        print(2**y)
        