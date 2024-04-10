
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

rows=len(grid)
cols=len(grid[0])

if not (rows and cols):
    print(0)

points=[]
row_c=[0]*rows
col_c=[0]*cols

for i in range(rows):
    for j in range(cols):
        if grid[i][j]==1:
            points.append((i,j))
            row_c[i]+=1
            col_c[j]+=1

ans=0

for r,c in points:
    if row_c[r]>1 or col_c[c]>1:
        ans+=1

print(ans)


