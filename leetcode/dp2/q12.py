
class Solution:
    def longestCommonSubsequence(self,text1:str,text2:str)->int:
        m=len(text1)
        n=len(text2)
        dp=[[-1 for i in range(n+1)] for _ in range(m+1)]

        def solve(pos1,pos2,text1,text2,dp):
            if pos1>=m or pos2>=n:
                return 0
            if dp[pos1][pos2]!=-1:
                return dp[pos1][pos2]
            
            if text1[pos1]==text2[pos2]:
                dp[pos1][pos2]=1+solve(pos1+1,pos2+1,text1,text2,dp)
                return dp[pos1][pos2]
            
            dp[pos1][pos2]=max(solve(pos1+1,pos2,text1,text2,dp),solve(pos1,pos2+1,text1,text2,dp))

            return dp[pos1][pos2]
        
        return solve(0,0,text1,text2,dp)
    


