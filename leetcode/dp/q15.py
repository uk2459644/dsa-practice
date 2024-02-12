# Jump problem bottom up approach

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False for i in range(n)]
        dp[0] = True

        for i in range(n):
            if dp[i]==False:
                break
            for j in range(i+1, i+nums[i]+1):
                if j == n-1:
                    return True
                if j > n-1:
                    return True
                if j < n-1:
                    dp[j] = True

        return dp[n-1]
