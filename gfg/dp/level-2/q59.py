
# A top-down DP implementation of LCS problem
m=1000
n=1000

dp=[[-1 for i in range(n+1)] for j in range(m+1)]

def lcs(X,Y,m,n,dp):
    if m==0 or n==0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    
    if X[m-1]==Y[n-1]:
        dp[m][n]=1+lcs(X,Y,m-1,n-1,dp)

        return dp[m][n]
    
    dp[m][n]=max(lcs(X,Y,m,n-1,dp),lcs(X,Y,m-1,n,dp))

    return dp[m][n]


