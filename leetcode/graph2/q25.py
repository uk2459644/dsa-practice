
grid = [[1,0,1],[0,0,0],[1,0,1]]

row=len(grid)
col=len(grid[0])

visited = [[0]*col for _ in range(row)]

direction=[(0,1),(1,0),(0,-1),(-1,0)]
ans=0

def bfs(x,y):
    global ans
    queue=[(0,x,y)]
    while queue:
        dst,r,c=queue.pop(0)
        if visited[r][c]==1:
            continue
        ans=max(ans,dst)
        visited[r][c]=1
        for dx,dy in direction:
            nr,nc=r+dx,c+dy
            if 0<=nr<row and 0<=nc<col and visited[nr][nc]==0:
                queue.append((dst+1,nr,nc))


points=[]
for i in range(row):
    for j in range(col):
        if grid[i][j]==1:
            points.append((i,j))



print(ans)








