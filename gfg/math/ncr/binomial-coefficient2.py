"""
Memoization Approach: The idea is to create a lookup table and follow
the recursive top-down approach. Before computing any value, we check
if it is already in the lookup table, if yes, we return the value.
Else we compute the value and store it in the lookup table.
"""
def binomialCoeffUtil(n,k,dp):
    # if value in lookup table then return
    if dp[n][k]!=-1:
        return dp[n][k]
    
    # store value in a table before return
    if k==0:
        dp[n][k]=1
        return dp[n][k]
    
    if k==n:
        dp[n][k]=1
        return dp[n][k]
    
    # save value in lookup table before return
    dp[n][k]=(binomialCoeffUtil(n-1,k-1,dp)+binomialCoeffUtil(n-1,k,dp))

    return dp[n][k]

def binomialCoeff(n,k):
    dp=[[-1 for i in range(k+1)] for j in range(n+1)]

    return binomialCoeffUtil(n,k,dp)
"""
Cancellation of factors between numerator and denominator:

nCr=(n-r+1)*(n-r+2)*...*n/(r!)

Create an array arr of numbers from n-r+1 to n which will be of size r.
As nCr is always an integer, all numbers in the denominator should cancel
with the product of the numerator.

for i=1 to i=r:
search arr, if arr[j] and i have gcd>1, divide both by gcd and when becomes 1,
stop the search.

Now answer is just the product of arr, whose value can be forund as
(a*b)%mod=(a%mod*b%mod)%mod

"""
import math

class GFG:
    def nCr(self,n,r):
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        
        if r>n:
            return 0
        if r>n-r:
            r=n-r
        mod=10**9+7

        arr=list(range(n-r+1,n+1))
        ans=1
        for i in range(1,r+1):
            j=0
            while j<len(arr):
                x=gcd(i,arr[j])
                if x>1:
                    arr[j]//=x
                    i//=x
                if arr[j]==1:
                    del arr[j]
                    j-=1
                if i==1:
                    break
                j+=1
        
        for i in arr:
            ans=(ans*i)%mod
        
        return ans
    
