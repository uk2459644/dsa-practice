"""
Given a matrix mat[][] of dimensions N*M, the task is to
find the size of the largest square submatrix such that the sum of all
rows, columns, diagonals in that submatrix are equal.

"""
"""
Approach: The given problem can be solved by finding the prefix sum of all 
the rows and the columns and then iterate for all possible sizes of the the square
submatrix from each cell of the matrix and if there exists any such square matrix
that satisfies the given criteria then print the size of the square matrix.

"""

# define the prefix sum array globally

prefix_sum_row=[[0]*51 for _ in range(50)]
prefix_sum_col=[[0]*50 for _ in range(51)]

def is_valid(r,c,size,grid):
    r_end=r+size
    c_end=c+size

    # Diagonal sum
    sum=0
    j=c 

    for i in range(r,r_end):
        sum+=grid[i][j]
        j+=1
    
    # Check each column
    for i in range(c,c_end):
        

