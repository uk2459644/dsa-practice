"""
Approach:
Instead of taking two separate dummy arrays, take the first row and column
of the matrix as the array for checking whether the particular column or row
has the value 1 or not. Since matrix[0][0] are overlapping. Therefore take
separate variable col0(say) to check if the 0th column has 1 or not and use
matrix[0][0] to check if the 0th row has 1 or not. Now traverse from the last
element to the first element and check if matrix[i][0]==1 || matrix[0][j]==1 and if true
set matrix[i][j]=1, else continue.

"""

def modifyMatrix(mat):
    row_flag=False
    col_flag=False

    # updating the first row and col if 1 is encountered
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            if (i==0 and mat[i][j]==1):
                row_flag=True
            
            if (j==0 and mat[i][j]==1):
                col_flag=True
            
            if (mat[i][j]==1):
                mat[0][j]=1
                mat[i][0]=1
                
