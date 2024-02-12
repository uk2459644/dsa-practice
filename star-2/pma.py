for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    sumli=list()
    minli=list()
    for i in range(n):
        if i%2==0:
            sumli.append(int(abs(li[i])))
        else:
            minli.append(int(abs(li[i])))
    mina=min(sumli)
    maxb=max(minli)

    if maxb>mina:
        ans=(sum(sumli)-mina)-(sum(minli)-maxb)
        ans+=(maxb-mina)
        print(ans)
    else:
        ans=sum(sumli)-sum(minli)
        print(ans)