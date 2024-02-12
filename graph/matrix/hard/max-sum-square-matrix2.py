"""
Approach2: Using Dynamic Programming

The approach used in this code is based on dynamic programming. A 2D dp table is
inialized and populated with the cumulative sum of the elements in the matrix. 
Then, for each possible submatrix of size, the sum is calculated by subtracting
the sum of the elements outside the submatrix. The maximum sum and the corresponding
submatrix are kept track of throughout the process. Finally, the submatrix with the
maximum sum is returned.

Algorithm:

1. Create a 2D DP array of the same size as the input matrix and initialize it
with the corresponding elements of the input matrix.

2. Compute the sum of elements in each submatrix of size sizexsize using the DP
array.

3. Find the maximum sum submatrix using the computed sums and return it.

"""

def max_sum_submatrix(matrix,size):
    rows=len(matrix)
    cols=len(matrix[0])

    dp=[[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            dp[i][j]=matrix[i][j]
            if i>0:
                dp[i][j]+=dp[i-1][j]
            
            if j>0:
                dp[i][j]+=dp[i][j-1]
            if i>0 and j>0:
                dp[i][j]-=dp[i-1][j-1]
    
    max_sum=float('-inf')
    for i in range(size-1, rows):
        for j in range(size-1, cols):
            submatrix_sum = dp[i][j]
            if i >= size:
                submatrix_sum -= dp[i-size][j]
            if j >= size:
                submatrix_sum -= dp[i][j-size]
            if i >= size and j >= size:
                submatrix_sum += dp[i-size][j-size]
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [row[j-size+1:j+1] for row in matrix[i-size+1:i+1]]
    return max_submatrix