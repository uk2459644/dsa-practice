
class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid:list[list[int]])->int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        dp=[[-1 for i in range(col)] for _ in range(row)]

        def solve(r,c,obstacles,dp):
            if r==row-1 and c==col-1 and obstacles[r][c]==0:
                dp[r][c]=1
                return dp[r][c]
            
            if r>=0 and r<row and c>=0 and c<col and dp[r][c]!=-1:
                return dp[r][c]
            
            if r>=0 and r<row and c>=0 and c<col and obstacles[r][c]==0:
                dp[r][c]=solve(r+1,c,obstacles,dp)+solve(r,c+1,obstacles,dp)
                return dp[r][c]
            else:
                return 0
        
        return solve(0,0,obstacleGrid,dp)
    
    
        
    


