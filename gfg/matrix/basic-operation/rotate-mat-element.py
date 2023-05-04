"""
Given a matrix, clockwise rotate elements in it.

The idea is to use loops similar to the program for printing
a matrix in spiral form. One by one rotate all rings of elements, starting
from the outermost. To rotate a ring, we need to do followinng.

1. Move elements of top row.
2. Move elements of last column.
3. Move elements of bottom row.
4. Move elements of first column.

Repeat above steps for inner ring while there is an inner ring.
"""
def rotateMatrix(mat):
    if not len(mat):
        return 
    
    top=0
    bottom=len(mat)-1

    left=0
    right=len(mat[0])-1

    while left<right and top<bottom:
        # store the first element of next row,
        # this element will replace first element of current row.
        prev=mat[top+1][left]
        # move elements of top row one step right
        for i in range(left,right+1):
            curr=mat[top][i]
            mat[top][i]=prev
            prev=curr
            
