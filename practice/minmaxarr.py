import itertools
import math

def minimize(nums):
    nums=list(itertools.accumulate(nums))
    return max((i+nums[i])//(1+i) for i in range(len(nums)))

def minimizeArrValue(nums):
    cum_sum=maximum=0
    for i, num in enumerate(nums,start=1):
        cum_sum+=num
        maximum=max(math.ceil(cum_sum/i),maximum)
    return maximum

for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    res=minimize(nli)
    print(res)