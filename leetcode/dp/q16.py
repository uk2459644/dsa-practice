class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n=len(arr)
        dp=[False for _ in range(n)]
        ans=False
        def dfs(i,n,nums):
            if dp[i]:
                return dp[i]
            if i>n:
                dp[n]=True
                return dp[n]
            
            if dp[i]==n:
                dp[i]==True
                return dp[i]
            
            if dp[i]==0:
                ans=True
            
            for e in range(1,nums[i]+1):
                if dfs(e+i,n,nums):
                    dp[i+e]=True
                    return True
            dp[i]=False
            return False
        dfs(start,n-1,arr)
        return ans
            