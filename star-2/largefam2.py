

for _ in range(int(input())):
    n=int(input())
    an_li=list(map(int,input().split()))
    an_li.sort()
    count=0
    sum=n-1 
    for a in an_li:
        if a <= sum:
            count+=1 
            sum-=a 
        else:
            break
    
    print(count)
