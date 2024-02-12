"""
Coin change using the Top Down Memoization Dynamic Programming: 

Follow the below steps to implement the idea: 

- Creating a 2-D vector to store the overlapping solutions
- Keep track of the overlapping subproblems while traversing the array coins[]

- Recall them whenever needed

"""

def coinchange(a,v,n,dp):
    if (v==0):
        dp[n][v]=1
        return dp[n][v]
    
    if n==0:
        return 0
    
    if dp[n][v]!=-1:
        return dp[n][v]
    
    if a[n-1]<=v:
        # either pick this coin or not
        dp[n][v]=coinchange(a,v-a[n-1],n,dp)+coinchange(a,v,n-1,dp)

        return dp[n][v]
    else:
        # we have no option but to leave this coin
        dp[n][v]=coinchange(a,v,n-1,dp)
        return dp[n][v]
    
