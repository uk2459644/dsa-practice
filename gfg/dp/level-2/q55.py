# Python program to counts Palindromic subsequence in 
# a given string using recursion

str='abcd'

dp=[[-1 for x in range(1000)] for y in range(1000)]

def countPS(i,j):
    if (i>j):
        return 0
    
    if(dp[i][j]!=-1):
        return dp[i][j]
    
    if i==j:
        dp[i][j]=1
        return dp[i][j]
    
    elif(str[i]==str[j]):
        dp[i][j]=(countPS(i+1,j)+countPS(i,j-1)+1)
        return dp[i][j]
    
    else:
        dp[i][j]=(countPS(i+1,j)+countPS(i,j-1)-countPS(i+1,j-1))

        return dp[i][j]
    


