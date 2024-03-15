
grid = [
    ["b","a","c"],
    ["c","a","c"],
    ["d","d","c"],
    ["b","c","c"]]

row = len(grid)
col = len(grid[0])

visited = set()
visited_val=list()

directions = [(0,1),(1,0),(0,-1),(-1,0)]


def dfs(i,j,parent,count):
    ans=False
    if 0<=i<row and 0<=j<col:
        if (i,j) not in visited:
            visited.add((i,j))
            for dx,dy in directions:
                if 0<=(i+dx)<row and 0<=(j+dy)<col and (i+dx,j+dy)!=parent:
                    if grid[i][j]==grid[i+dx][j+dy]:
                        visited_val.append(grid[i][j])
                        ans |=dfs(i+dx,j+dy,(i,j),count+1)
        elif (i,j) in visited and count>=4:
            return True
    return ans

ans=False
for i in range(row):
    for j in range(col):
        if (i,j) not in visited and not ans:
            ans |=dfs(i,j,(-1,-1),0)


print(ans,visited_val)




