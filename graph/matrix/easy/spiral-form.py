"""
Draw the path that the spiral makes. We know that the path should 
turn clockwise whenever it would go out of bounds or into a cell that
was previously visited.
"""
"""
Steps to solve the problem:
- Let the array have R rows and C columns

"""
def spiralOrder(matrix):
    ans=[]
    if (len(matrix)==0):
        return ans
    m=len(matrix)
    n=len(matrix[0])
    seen=[[0 for i in range(n)] for j in range(m)]
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    x=0
    y=0
    di=0
    for i in range(m*n):
        ans.append(matrix[x][y])
        seen[x][y]=True
        cr=x+dr[di]
        cc=y+dc[di]
        if (0<=cr and cr<m and 0<=cc and )
