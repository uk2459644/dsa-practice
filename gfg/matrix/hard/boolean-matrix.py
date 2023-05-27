"""
Given a boolean matrix mat[m][n] of size mXn, modify it such that if a 
matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and
jth column as 1.

Approach: Using Brute Force

Assuming all the elements in the matrix are non-negative. Traverse through
the matrix and if you find an element with value 1, then change all the elements
in its row and column to -1, except when an element is 1. The reason or not
changing other elements to 1, but -1, is because that might affect other columns
and rows. Now traverse through the matrix again and if an element is -1 change it to
1, which will be the answer.

"""
def setZeroes(matrix):
    # get the length of the matrix
    rows=len(matrix)
    cols=len(matrix[0])

    # Iterate through each element of the matrix
    for i in range(0,rows):
        for j in range(0,cols):
            # if the element is 1, mark its corresponding row and column using -1
            if matrix[i][j]==1:
                # mark all elements in the same column as -1, except for other 1's
                ind=i-1
                while ind>=0:
                    if matrix[ind][j]!=1:
                        matrix[ind][j]=-1
                    ind-=1
                
                ind=i+1
                while ind<rows:
                    if matrix[ind][i]!=1:
                        matrix[ind][i]=-1
                    ind+=1 
                
                # mark all elements in the same row as -1, except for other 1's
                ind=j-1
                while ind>=0:
                    if matrix[i][ind]!=1:
                        matrix[i][ind]=-1
                    ind-=1
                
                ind=j+1
                while ind<cols:
                    if matrix[i][ind]!=1:
                        matrix[i][ind]=-1
                    ind+=1 
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j]<0:
                matrix[i][j]=1
                
