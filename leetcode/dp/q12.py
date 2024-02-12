class Solution:
    def canJump(self,nums:list)->bool:
        n=len(nums)
        if n==1:
            return True
        
        x=[nums[i]+i for i in range(n)]
        maxi=x[0]
        ans=True

        for i in range(n):
            if x[i]>i:
                if x[i]>maxi:
                    maxi=x[i]
            elif maxi==n-1:
                ans=True
                break
            else:
                if maxi<=i:
                    ans=False
                    break
        
        return ans




