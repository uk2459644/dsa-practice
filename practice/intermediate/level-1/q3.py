from collections import Counter

for _ in range(int(input())):
    n=int(input())
    numbers=list(map(int,input().split()))
    nums=Counter(numbers)
    max=nums.most_common()[0][1]
    total=len(numbers)
    
    print(total-max)
