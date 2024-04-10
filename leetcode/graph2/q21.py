import heapq

grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2,5]
start = [0,0]
k = 3

queue=[]

row = len(grid)
col = len(grid[0])

visited=set()

direction=[(0,1),(1,0),(0,-1),(-1,0)]
sx,sy=start[0],start[1]
l,h=pricing[0],pricing[1]

heapq.heappush(queue,(0,grid[sx][sy],sx,sy))
ans=[]
while queue:
    dst,price,r,c=heapq.heappop(queue)
    if (r,c) in visited:
        continue
    visited.add((r,c))
    if len(ans)==k:
        return ans
    if l<=price<=h:
            ans.append([r,c])
    for dx,dy in direction:
        rn,cn=r+dx,c+dy
        if 0<=rn<row and 0<=cn<col and grid[rn][cn]!=0:
            heapq.heappush(queue,(dst+1,grid[rn][cn],rn,cn))
           
# print(ans)
return ans


    




