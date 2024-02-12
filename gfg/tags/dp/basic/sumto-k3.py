"""
Efficient Approach: Using DP tabulation method (iterative approach)

The approach to solve this problem is same but DP tabulation (bottom-up)
method is better then Dp+memoization because memoization method needs extra
stack space of recursion calls. 

Steps to solve this problem:

- Create a table DP to store the solution of the subproblems.
- Initialize the table with base cases.
- Now iterate over subproblems to get the value of current problem form
  previous computation of subproblems stored in DP
- Return the final solution stored in.

"""

def maxSum(a,n,k):
    # Initialize the DP table
    dp=[[0 for i in range(k+1)] for j in range(n+1)]
    # Fill in the DP table in bottom up manner
    for i in range(1,n+1):
        for j in range(1,k+1):
            # Don't pick the current element 
            dp[i][j]=dp[i-1][j]
            # Pick the current element
            if j>=a[i-1]:
                dp[i][j]=max(dp[i][j],a[i-1]+dp[i-2][j-a[i-1]])
    
    return dp[n][k]



