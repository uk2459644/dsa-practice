for _ in range(int(input())):
    n=int(input())
    k=n//2
    l,r=k+1,k
    ali=list()
    for i in range(n):
        if i%2==0:
            ali.append(r+1)
            r+=1
        else:
            ali.append(l-1)
            l-=1
    
    print(*ali)