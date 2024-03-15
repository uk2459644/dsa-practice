
grid=[[1,1,1,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]

rw=len(grid)
cl=len(grid[0])

visited=[[False for i in range(cl)] for j in range(rw)]
paths=list()

def dfs(r,c):
    if r>=0 and c>=0 and r<rw and c<cl:
        if not visited[r][c] and grid[r][c]==1:
            if r==rw-1 and c==cl-1:
                paths.append(1)
            else:
                # if r!=0 or c!=0:
                visited[r][c]=True
                dfs(r+1,c)
                dfs(r,c+1)

dfs(0,0)

print(paths,visited)

if len(paths)>1:
    print(False)
else:
    print(True)




