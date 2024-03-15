from collections import deque
import math

grid = [
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

row=len(grid)
col=len(grid[0])

queue=deque([(0,0,0)])

visited=set()



def mhd(r,c):
    dst=math.inf
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                dst=min(dst,abs(r-i)+abs(c-j))
    
    return dst

ans = -1
directions=[(1,0),(0,1),(-1,0),(0,-1)]
while queue:
    distance,r,c=queue.popleft()
    if (r,c)==(row-1,col-1):
        ans=max(ans,distance)
        continue

    for rw,cl in directions:
        nr,nc=r+rw,c+cl
        if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited:
            visited.add((nr,nc))
            ndistance=max(distance,mhd(nr,nc))
            queue.append((ndistance,nr,nc))

print(ans)



