n=4
m=4

dp=[[0 for i in range(n+1)] for _ in range(m+1)]

def numberOfPaths(n,m,dp):
    if (n==1 or m==1):
        dp[n][m]=1
        return 1
# Add the element in the DP table if it was not computed before
    if (dp[n][m]==0):
        dp[n][m]=numberOfPaths(n-1,m,dp)+numberOfPaths(n,m-1,dp)
    
    return dp[n][m]


