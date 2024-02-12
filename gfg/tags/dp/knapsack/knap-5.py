"""
Efficient approach: Using DP Tabulation method (Iterative approach)

The approach to solve this problem is same but DP tabulation method is better
than memoization(top-down) because memoization method needs extra stack space of recursion
calls.

Steps to solve this problem: 
- Create a DP to store the solution of the subproblems and initialize it with 0.
- Initialize the DP with base cases
- Now iterate over subproblems to get the value of current problem form previous
  computaion of subproblem stored in DP.

- After filling the DP now in main function call every query and get the answer
  stored in DP.


"""

import sys 

# Function to compute the maximum value that can be obtained
# from the knapsack within the given capacity

def findMax(w,n,c):
    # initializing the dp table with 0
    dp=[[0 for j in range(c+1)] for i in range(n+1)]

    # Filling the DP table bottom-up
    for i in range(1,n+1):
        for j in range(1,c+1):
            if w[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]]+w[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp

# Driver code 
if __name__=="__main__":
    # Input array
    w=[3,8,9]
    n=len(w)

    # all given queries
    queries=[11,10,4]
    q=len(queries)
    # find maximum
    ma=max(queries)

    # function call 
    dp=findMax(w,n,ma)
    # perform queries
    for i in range(q):
        print(dp[n][queries[i]])
        

