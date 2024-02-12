"""
Given a matrix, swap the element of major and minor diagonals.

The Major Diagonal Elements of a Matrix:
The Major Diagonal elements are the ones that occur from Top Left of
Matrix Down To Bottom Right Corner.

Minor Diagonal :
The minor diagonal elements are the ones that occur from top right of
matrix down to bottom left corner.
"""
def swapDiagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i],matrix[i][len(matrix)-i-1]=matrix[i][len(matrix)-i-1],matrix[i][i]
        

