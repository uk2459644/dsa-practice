import math
from collections import deque
import heapq

grid = [[0,0,1],[0,0,0],[0,0,0]]

theives = list()

row = len(grid)
col = len(grid[0])

for i in range(row):
    for j in range(col):
        if grid[i][j]:
            theives.append((i,j))

dist=[[math.inf for i in range(col)] for j in range(row)]

directions = [(0,1),(1,0),(0,-1),(-1,0)]

for x,y in theives:
    queue=deque([(x,y,0)])
    visited=set()
    while queue:
        r,c,dst=queue.popleft()
        if (r,c) in visited:
            continue 
        visited.add((r,c))
        if dst>dist[r][c]:
            continue
        dist[r][c]=dst
        for dx,dy in directions:
            nr,nc=r+dx,c+dy
            if 0<=nr<row and 0<=nc<col:
                queue.append((nr,nc,dst+1))


h=[(-dist[0][0],0,0)]
visited=set([(0,0)])

res=float('inf')
while h:
    d,r,c=heapq.heappop(h)
    res=min(res,-d)
    if r==row-1 and c==col-1:
        # return res
        print(res)
    
    for dx,dy in directions:
        nr,nc=r+dx,c+dy
        if 0<=nr<row and 0<=nc<col:
            if (nr,nc) in visited:
                continue
            visited.add((nr,nc))
            heapq.heappush(h,(-dist[nr][nc],nr,nc))

