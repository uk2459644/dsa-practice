def solve(nums:list):
    x=[nums[i]+i for i in range(len(nums))]
    # each element in this represent max index that can be reached
    l,r,jumps=0,0,0
    while r<len(nums)-1:
        jumps+=1
        l,r=r+1,max(x[l:r+1])
    
    return jumps