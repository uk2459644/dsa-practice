
for _ in range(int(input())):
    n,m=map(int,input().split())
    opening_times=[1]*2000
    person_li=list()

    for i in range(n):
        low,high=list(map(int,input().split()))
        li=[0]*(high-low)
        opening_times=opening_times[:low]+li+opening_times[high:]
    
    for i in range(m):
        p=int(input())
        ans_li=opening_times[p:]
        if ans_li[0]==0:
            print(0)
        elif 0 in ans_li:
            print(ans_li.index(0))
        else:
            print(-1)
       
    

    
    