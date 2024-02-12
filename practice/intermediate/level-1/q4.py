from collections import Counter 

for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    set_nli=set(nli)
    if len(set_nli)==1:
        print("YES")
    else:
        nums=Counter(nli)
        ans1=nums.most_common()[0][1]
        ans2=nums.most_common()[1][1]
        if ans1!=ans2:
            print("YES")
        else:
            print("NO")

