
grid = [[0,13,1,7,20],[3,8,19,12,15],[18,2,14,21,6],[9,4,23,16,11],[24,17,10,5,22]]

rw=cl=len(grid)

visited = [[False for i in range(rw)] for i in range(cl)]

li=list()
def dfs(r,c):
    if r>=0 and c>=0 and r<rw and c<cl:
        if not visited[r][c]:
            visited[r][c]=True
            li.append(True)
            dfs(r+2,c+1)
            dfs(r+2,c-1)
            dfs(r-2,c+1)
            dfs(r-2,c-1)
            dfs(r+1,c+2)
            dfs(r-1,c+2)
            dfs(r+1,c-2)
            dfs(r-1,c-2)


dfs(0,0)

if len(li)==rw*rw:
    print(True)
else:
    print(False)



