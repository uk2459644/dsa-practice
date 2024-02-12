
for i in range(int(input())):
    n,k=map(int,input().split())
    c=0
    o=0
    l=list(map(int,input().split()))
    for j in range(n-k+1):
        for h in range(j,j+k):
            if (l[h]%2==1):
                o=1
                break
        if o==1:
            c+=1
        o=0
    print(c)


