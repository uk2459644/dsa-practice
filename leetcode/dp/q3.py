
class Solution:
    def minCostClimbingStairs(self,cost:list)->int:

        if not cost:
            return 0
        
        n=len(cost)
        dp=[0]*n

        dp[0]=cost[0]
        if n>=2:
            dp[1]=cost[1]
        
        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        
        return min(dp[-1],dp[-2])




