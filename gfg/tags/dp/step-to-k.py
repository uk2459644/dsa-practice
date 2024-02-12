"""
Given a positive integer k, the task is to find the minimum number
of operations of the following two types, required to change 0 to k.

"""

"""
Approach: 
* If K is an odd number, the last step must be adding 1 to it.
* if k is an even number, the last step is to multiply by 2 to minimize the number of steps
* Create a dp[] table that stores in every dp[i], the minimum steps required to reach i.

"""

# Function to find minimum operations

def minOperation(k):
    # dp is initialized to store the steps
    dp=[0]*(k+1)

    for i in range(1,k+1):
        dp[i]=dp[i-1]+1

        # For all even numbers
        if (i%2==0):
            dp[i]=min(dp[i],dp[i//2]+1)
    
    return dp[k]



