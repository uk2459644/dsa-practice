
grid = [
    [0,0,1,1,0,1,0,0,1,0],
    [1,1,0,1,1,0,1,1,1,0],
    [1,0,1,1,1,0,0,1,1,0],
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,1,0,1,0,1],
    [1,1,1,0,1,1,0,1,1,0]
    ]
row=len(grid)
col=len(grid[0])

direction=[(0,1),(1,0),(0,-1),(-1,0)]

def dfs(x,y):
    grid[x][y]=1
    for dx,dy in direction:
        r,c=x+dx,y+dy
        if 0<=r<row and 0<=c<col and grid[r][c]==0:
            dfs(r,c)


for i in range(row):
    for j in range(col):
        if i==0 or j==0:
            if grid[i][j]==0:
                dfs(i,j)
            
        if i==(row-1) or j==(col-1):
            if grid[i][j]==0:
                dfs(i,j)


ans=0
for i in range(row):
    for j in range(col):
        if grid[i][j]==0:
            ans+=1
            dfs(i,j)

print(ans)
