
class Solution:
    def minPathSum(self,grid:list[list[int]])->int:
        row=len(grid)
        col=len(grid[0])
        dp=[[-1 for _ in range(col)] for i in range(row)]

        def solve(r,c,grid):
            if r==row-1 and c==col-1:
                dp[r][c]=grid[r][c]
                return dp[r][c]
            
            if r>=0 and r<row and c>=0 and c<col and dp[r][c]!=-1:
                return dp[r][c]
            
            if r>=0 and r<row and c>=0 and c<col:
                dp[r][c]=grid[r][c]+min(solve(r+1,c,grid),solve(r,c+1,grid))
                return dp[r][c]
            elif r==row and c<col:
                dp[r-1][c]=grid[r-1][c]+solve(r-1,c+1,grid)
                return dp[r-1][c]
            elif c==col and r<row:
                dp[r][c-1]=grid[r][c-1]+solve(r+1,c-1,grid)
                return dp[r][c-1]
        
        return solve(0,0,grid)
    

