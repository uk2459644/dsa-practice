"""
Minimize steps to reach k from 0 by adding 1 or dubbling at each steps.

Given a positive integer K, the task is to find the minimum number of operations
of the following two steps, required to change  0 to k.

- Add one to the operand
- Multiply the operand by 2
"""

# Function to find minimum operations

def minOperation(k):
    # dp is initialised to store the steps
    dp=[0]*(k+1)

    for i in range(1,k+1):
        dp[i]=dp[i-1]+1

        # For all even numbers
        if(i%2==0):
            dp[i]=min(dp[i],dp[i//2]+1)
    
    return dp[k]

