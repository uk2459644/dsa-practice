
for _ in range(int(input())):
    n=int(input())
    an_li=list(map(int,input().split()))
    an_li.sort()
    count=0
    for i in range(n):
        if i==an_li[i]:
            count+=1 
    print(count)

