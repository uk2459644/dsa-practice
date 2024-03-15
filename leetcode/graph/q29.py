

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 =[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

row = len(grid2)
col = len(grid2[0])

def dfs(r:int,c:int):
    ans=True
    if r>=0 and c>=0 and r<row and c<col and grid2[r][c]==1:
        grid2[r][c]=0
        ans1=dfs(r+1,c)
        ans2=dfs(r,c+1)
        if grid1[r][c]==1:
            return True
        else:
            return False

    return ans

count=0
for i in range(row):
    for j in range(col):
        if grid2[i][j]==1:
            ans=dfs(i,j)
            if ans:
                count+=1

print(count)



