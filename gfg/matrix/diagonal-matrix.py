"""
Given a 2D square matrix, print the Principal and
Secondary diagonals.

Solution: 
The primary diagonal is formed by the elements A00, A11, A22, A33.
Condition for Principal Diagonal: The row-column condition is row=column.

The secondary diagonal is formed by the elements A03, A12, A21, A30.

Condition for Secondary Diagonal: The row-column condition is 
row=numberOfRows-column-1
"""
MAX=100

def printPrincipalDiagonal(mat,n):
    print("Principal Diagonal: ", end="")
    for i in range(0,n):
        for j in range(0,n):
            if (i==j):
                print(mat[i][j],", ",end="")
    
    print("")

def printSecondaryDiagonal(mat,n):
    print("Secondary Diagonal: ",end="")
    for i in range(0,n):
        for j in range(0,n):
            # condition for secondary diagonal
            if ((i+j)==(n-1)):
                print(mat[i][j],", ",end="")
    print("")

