
n=1001
m=1001

dp=[[-1 for i in range(m+1)] for i in range(n+1)]


def minDis(s1,s2,n,m,dp):
    # if any string is empty
    # return the remaining characters of other string
    if n==0:
        return m
    if m==0:
        return n
    
    # To check if the recursive tree for given n & m has already
    # been executed
    if dp[n][m]!=-1:
        return dp[n][m]
    
    # If characters are equal, execute recursive function for n-1,m-1
    if s1[n-1]==s2[m-1]:
        if dp[n-1][m-1]==-1:
            dp[n][m]=minDis(s1,s2,n-1,m-1,dp)
            return dp[n][m]
        else:
            dp[n][m]=dp[n-1][m-1]
            return dp[n][m]
    
    # If characters not equal, we need to find the minimum cost
    # out of all 3 operations
    else:
        if dp[n-1][m]!=-1:
            m1=dp[n-1][m]
        else:
            m1=minDis(s1,s2,n-1,m)
        
        if dp[n][m-1]!=-1:
            m2=dp[n][m-1]
        else:
            m2=minDis(s1,s2,n,m-1)
        
        if dp[n-1][m-1] !=-1:
            m3=dp[n-1][m-1]
        else:
            m3=minDis(s1,s2,n-1,m-1)

        dp[n][m]=1+min(m1,m2,m3)
        return dp[n][m]
    
