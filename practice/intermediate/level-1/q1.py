for _ in range(int(input())):
    n=int(input())
    nli=list()
    for i in range(n):
        num=int(input())
        nli.append(num)
    nli.sort()

    for j in range(0,n-1,2):
        if nli[j]!=nli[j+1]:
            print(nli[j])
            break
