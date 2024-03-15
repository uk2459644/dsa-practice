
grid=[[4]]

rw=len(grid)
cl=len(grid[0])

visited=[[False for i in range(cl)] for j in range(rw)]

def dfs(r,c):
    ans=0
    if r>=0 and c>=0 and r<rw and c<cl:
        if not visited[r][c]:
            visited[r][c]=True
            if grid[r][c]!=0:
                ans+=grid[r][c]
                ans+=dfs(r,c+1)
                ans+=dfs(r,c-1)
                ans+=dfs(r+1,c)
                ans+=dfs(r-1,c)
    
    return ans

mx_ans=0

for i in range(rw):
    for j in range(cl):
        mx_ans=max(mx_ans,dfs(i,j))

print(mx_ans)







