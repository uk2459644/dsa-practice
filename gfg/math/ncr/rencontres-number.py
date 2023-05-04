"""
Given two numbers, n>=0 and 0<=k<=n, count the number of derangements with
k fixed points.

D(n,k) represents count of partial derangements.

D(0,0)=1
D(0,1)=0
D(n+2,0)=(n+1)*(D(n+1,0)+D(n,0))
D(n,k)=nCk*D(n-k,0)

"""

def binomialCoeff(n,k):
    if (k==0 or k==n):
        return 1
    
    return (binomialCoeff(n-1,k-1)+binomialCoeff(n-1,k))

# returns recontres number D(n,m)

def RecontresNumber(n,m):
    # base condition
    if (n==0 and m==0):
        return 1
    
    # base condition
    if (n==1 and m==0):
        return 0
    
    # base condition
    if m==0:
        return ((n-1)*(RecontresNumber(n-1,0)+RecontresNumber(n-2,0)))
    
    return (binomialCoeff(n,m)*RecontresNumber(n-m,0))

