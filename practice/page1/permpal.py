for _ in range(int(input())):
    srng=input()
    srli=list(srng)
    n=len(srli)
    lst=list()
    odd=0
    oddli=[]
    dct=dict()
    psbl=True
    for i in range(n):
        if srli[i] in dct.keys():
            dct[srli[i]].append(i+1)
        else:
            dct[srli[i]]=[i+1]
    
    for key,value in dct.items():
        if len(value)%2==0:
            md=len(lst)//2
            lst=lst[:md]+value+lst[md:]
        else:
            odd+=1 
            oddli=value
            if odd>1:
                psbl=False
                break
    if psbl:
        if odd==0:
            print(*lst)
        else:
            md=len(lst)//2
            lst=lst[:md]+oddli+lst[md:]
            print(*lst)
    else:
        print(-1)