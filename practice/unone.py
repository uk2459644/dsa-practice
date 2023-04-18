for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    odli=list()
    evli=list()
    for a in nli:
        if (a&1):
            odli.append(a)
        else:
            evli.append(a)
    lst=evli+odli
    print(*lst)