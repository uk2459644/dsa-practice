"""
Given 3 strings of all having length < 100, the task
is to find the longest common sub-sequence in all three
given sequences.

Approach: 

The idea is to take a 3D array to store the length of common subsequence
in all 3 given sequence, L[m+1][n+1][o+1]

1. If any of the string is empty then there is no common subsequence at all
   then L[i][j][k]=0

2. If the characters of all sequence match or (X[i]==Y[j]==Z[k]) then
   L[i][j][k]=1+L[i-1][j-1][k-1]

3. If the characters of both sequence do not match or 
  (X[i]!=y[j] || X[i]!=Z[k] || Y[j]!=Z[k]) then 
  L[i][j][k]=max(L[i-1][j][k],L[i][j-1][k],L[i][j][k-1])
  
"""

def lcsOf3(X,Y,Z,m,n,o):
    L=[[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
    '''
    Following steps build L[m+1][n+1][o+1] in bottom up fashion. Note that
    L[i][j][k] contains length of LCS of X[0..i-1] and Y[0..j-1] and Z[0...k-1].
    '''

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i==0 or j==0 or k==0 ):
                    L[i][j][k]=0
                elif (X[i-1]==Y[j-1] and X[i-1]==Z[k-1]):
                    L[i][j][k]=L[i-1][j-1][k-1]+1 
                else:
                    L[i][j][k]=max(L[i-1][j][k],L[i][j-1][k],L[i][j][k-1])
    
    return L[m][n][o]

"""
Another Approach: 
using Recursion
"""
dp=[[[-1 for i in range(100)] for j in range(100)] for k in range(100)]

# Returns length of LCS for X[0..m-1], Y[0..n-1] and Z[0..o-1]
def lcsOf3(i,j,k):
    if (i==-1 or j==-1 or k==-1):
        return 0
    if (dp[i][j][k]!=-1):
        return dp[i][j][k]
    
    if (X[i]==Y[j] and Y[j]==Z[k]):
        dp[i][j][k]=1+lcsOf3(i-1,j-1,k-1)
        return dp[i][j][k]
    else:
        dp[i][j][k]=max(max(lcsOf3(i-1,j,k),lcsOf3(i,j-1,k)),lcsOf3(i,j,k-1))

        return dp[i][j][k]
    

            


