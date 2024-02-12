"""
Given an integer matrix of odd dimensions. the task is to find the
sum of the middle row & column elements.
"""
def middleSum(mat,n):
    row_sum=0
    col_sum=0

    for i in range(n):
        row_sum+=mat[n//2][i]
    
    print("Sum of middle row= ", row_sum)

    for i in range(n):
        col_sum+=mat[i][n//2]

"""
Method 2: Using STL
Here we use the accumulate function to do it.
"""

