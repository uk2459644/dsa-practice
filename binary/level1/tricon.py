import math 

for _ in range(int(input())):
    sum_n = int(input())
    level1=(-1+math.sqrt(1+8*sum_n))/2
    n=int(math.floor(level1))
    print(n)
    