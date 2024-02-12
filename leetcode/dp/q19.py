
nums=list(map(int,input().split()))
n=len(nums)

dp=[-1]*n

def solve(nums,pos,dp,n):
    if pos>n:
        return 0
    if pos==n:
        dp[pos]=nums[pos]
        return dp[pos]
    if dp[pos]!=-1:
        return dp[pos]
    dp[pos]=max(nums[pos]+solve(nums,pos+2,dp,n),solve(nums,pos+1,dp,n))
    return dp[pos]


solve(nums,0,dp,n-1)

