import math
import heapq

heights = [[1,2,2],[3,8,2],[5,3,5]]

row = len(heights)
col = len(heights[0])

dist=[[math.inf for i in range(col)] for j in range(row)]

direction=[(1,0),(0,1),(-1,0),(0,-1)]

queue = [(0,0,0)]

dist[0][0]=0

ans=list()
while queue:
    effort,r,c = heapq.heappop(queue)

    if r==(row-1) and c==(col-1):
        # return effort
        print(effort)
        # ans.append(effort)
    
    for dr,dc in direction:
        new_row,new_col = r+dr,c+dc

        if 0<= new_row < row and 0<= new_col < col:
            new_effort = max(effort,abs(heights[new_row][new_col]-heights[r][c]))
            if new_effort < dist[new_row][new_col]:
                dist[new_row][new_col]=new_effort
                heapq.heappush(queue,(new_effort,new_row,new_col))

print(ans,dist)


