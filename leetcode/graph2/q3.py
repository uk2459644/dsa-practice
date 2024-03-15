from collections import deque

grid = [[1,1,2]]

row = len(grid)
col = len(grid[0])

directions={
    1:[(0,1),(0,-1)],
    2:[(1,0),(-1,0)],
    3:[(0,-1),(1,0)],
    4:[(0,1),(1,0)],
    5:[(0,-1),(-1,0)],
    6:[(-1,0),(0,1)]
}

move={
    1:[1,3,5,4,6],
    2:[2,3,5,4,6],
    3:[1,2,4,6,5],
    4:[1,2,6,3,5],
    5:[1,2,3,4,6],
    6:[1,2,3,4,5]
}

queue=deque([(0,0)])
visited = set()
visited.add((0,0))

while queue:
    x,y=queue.popleft()
    if x==(row-1) and y==(col-1):
        print(True)
    for dx,dy in directions[grid[x][y]]:
        r,c=x+dx,y+dy
        if 0<=r<row and 0<=c<col and (r,c) not in visited and grid[r][c] in move[grid[x][y]]:
            visited.add((r,c))
            queue.append((r,c))

print(False)



