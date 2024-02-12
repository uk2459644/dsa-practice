# Jump problem top down approach

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [None for i in range(n)]
        def dfs(i, n, nums):

            if dp[i] != None:
                return dp[i]

            if i > n:
                dp[n] = True
                return dp[n]
            if i == n:
                dp[i] = True
                return dp[i]

            for e in range(1, nums[i]+1):
                if dfs(e+i, n, nums):
                    dp[i+e] = True
                    return True

            dp[i] = False
            return False

        dfs(0, len(nums)-1, nums)

        return dp[n-1]
