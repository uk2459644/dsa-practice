
class Solution:
    def generateParenthesis(self,n:int)->list[str]:
        res=[]
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]

        def dfs(left,right,s):
            if len(s)==2*n:
                dp[left][right]=s
                res.append(s)
                return
            if dp[left][right]!=-1:
                return dp[left][right]
            
            if left<n:
                 dp[left][right]=dfs(left+1,right,s+'(')
            
            if right<left:
                dp[left][right]=dfs(left,right+1,s+')')
        
        dfs(0,0,'')
        return res
    


