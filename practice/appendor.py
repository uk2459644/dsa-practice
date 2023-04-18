from  operator import ior 
import functools

for _ in range(int(input())):
    n,y=map(int,input().split())
    nli=list(map(int,input().split()))
    nli.sort(reverse=True)
    res=functools.reduce(ior,nli)
    # res=any(nli)
    num=''
    yst="{0:b}".format(y)
    psbl=True
    while (y) or res:
        if y&1==1:
            if res&1:
                num+='0'
            else:
                num+='1'
        if y&1==0:
            if res&1:
                psbl=False
                break
                # num+='0'
            else:
                num+='0'
        y>>=1
        res>>=1
    
    if psbl:
        num=num[::-1]
        print(int(num,2))
    else:
        print(-1)
   