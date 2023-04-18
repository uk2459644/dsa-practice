from math import factorial

for _ in range(int(input())):
    n,k=map(int,input().split())
    nli=sorted(list(map(int,input().split())))
    inq_lst=nli[:k]
    nm=inq_lst[-1]
    cnt=inq_lst.count(nm)
    cnt2=nli.count(nm)
    a=factorial(cnt2)
    b=factorial(cnt)*factorial(cnt2-cnt)

    print(a/b)