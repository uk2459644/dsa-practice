
grid = [[1,0,1],[0,0,0],[1,0,1]]

n=len(grid)
queue=[]

for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            queue.append((i,j))

if not queue or len(queue)==n*n:
    # return -1
    print(-1)

res=-1
direction=[(0,1),(1,0),(0,-1),(-1,0)]

while queue:
    res+=1
    size=len(queue)
    while size:
        size-=1
        x,y=queue.pop(0)
        for dx,dy in direction:
            r,c=x+dx,y+dy
            if 0<=r<n and 0<=c<n and grid[r][c]==0:
                grid[r][c]=1
                queue.append((r,c))

print(res)

