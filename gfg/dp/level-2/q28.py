# Dynamic programming solution for Matrix chain multiplication using
# Memoization

"""
If observed carefully you can find the following two properties:

1-> Optimal Substructure: In the above case, we are breakinng the bigger
    groups into smaller subgroups and solving them to finally find the 
    minimum number of multiplications. Therefore, it can be said that the
    problem has optimal substructure property.

2-> Overlapping Subproblems: We can see in the recursion tree that the same
    subproblems are called again and again and this problem has the Overlapping
    Subproblems property.

    So Matrix Chain Multiplication problem has both properties of a dynamic programming
    problem. So recomputations of same subproblems can be avoided by constructing a temporary
    array dp[][] in a bottom up manner.

"""

"""
Follow the below steps to solve the problem: 
- Build a matrix dp[][] of size N*N for memoization purposes. 
- USe the same recursive call as done in the above approach: 
  - When we find a range (i,j) for which the value is already calculated,
    return the minimum value for that range (i.e., dp[i][j])

  - Otherwise, perform the recursive calls as mentioned earlier.

The value stored at dp[0][N-1] is the required answer.
"""
# Python program using memoization
import sys 

dp=[[-1 for i in range(100)] for j in range(100)]

# Function for matrix chain multiplication 
def matrixChainMemoised(p,i,j):
    if i==j:
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]
    
    dp[i][j]=sys.maxsize

    for k in range(i,j):
        dp[i][j]=min(dp[i][j],matrixChainMemoised(p,i,k)+matrixChainMemoised(p,k+1,j)+p[i-1]*p[k]*p[j])
    
    return dp[i][j]




