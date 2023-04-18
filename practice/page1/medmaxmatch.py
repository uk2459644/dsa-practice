for _ in range(int(input())):
    n=int(input())
    ali=list(map(int,input().split()))
    bli=list(map(int,input().split()))
    ali.sort()
    bli.sort()
    k=n//2
    ali=ali[k:]
    bli=bli[k:]
    lst=list()
    ln=len(ali)
    for i in range(ln):
        a=ali[i]+bli[ln-i-1]
        lst.append(a)
    lst.sort()
    print(lst[0])

