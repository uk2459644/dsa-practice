
from functools import reduce


for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    mx=0
    for i in range(n):
        test_1=nli[i:]
        xor_1=0
        xor_2=0
        if len(test_1)>0:
            xor_1=reduce(lambda x,y:x^y,test_1)
        test_2=nli[:i]
        if len(test_2)>0:
            xor_2=reduce(lambda x,y:x^y,test_2)
        xor_value=xor_2+xor_1
        # xor_value=mx+xor_value
        mx=max(mx,xor_value)
    
    print(mx)
    