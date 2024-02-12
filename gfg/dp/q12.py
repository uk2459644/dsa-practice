"""
Dynamic programming - minimum number of deletion and insertion
using memoization technique
"""
dp=[[-1 for i in range(1001)] for j in range(1001)]

# returns length of longest common subsequence
def lcs(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]
    
    if s1[i-1]==s2[j-1]:
        dp[i][j]=1+lcs(s1,s2,i-1,j-1)
    else:
        dp[i][j]=max(lcs(s1,s2,i,j-1),lcs(s1,s2,i-1,j))
        return dp[i][j]
    

