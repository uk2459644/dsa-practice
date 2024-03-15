
land = [[1,0,0],[0,1,1],[0,1,1]]

row=len(land)
col=len(land[0])

def dfs(r,c):
    if r<0 or c<0 or r>=row or c>=col or land[r][c]==0:
        return (0,0)
    land[r][c]=0
    rr,rc=dfs(r+1,c)
    cr,cc=dfs(r,c+1)

    return (max(rr,cr,r),max(rc,cc,c))

ans=list()
for i in range(row):
    for j in range(col):
        x,y=dfs(i,j)
        ans.append([i,j,x,y])





