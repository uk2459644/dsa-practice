"""
Program to find minimum step to delete a string 
method returns minimum step for deleting the string, where in one
step a palindrome is removed

"""

def minStepToDeleteString(str):
    N=len(str)
    # declare dp array and initialize it with 0s
    dp=[[0 for x in range(N+1)] for y in range(N+1)]
    # loop for substring length we are considering
    for l in range(1,N+1):
        # loop with two variables i and j, denoting starting and ending
        # of substrings 
        i=0
        j=i-1 
        while j<<N:
            # if substring length is 1, then 1 step will be needed
            if (l==1):
                dp[i][j]=1
            else:
                # delete the ith char individually and assign result for
                # subproblem (i+1,j)
                dp[i][j]=1+dp[i+1][j]
                # if current and next char are same, choose min from current
                # and subproblem (i+2,j)
                if (str[i]==str[i+1]):
                    dp[i][j]=min(1+dp[i+2][j],dp[i][j])
                    '''
                    Loop over all right character and suppose kth char is same as
                    ith character then choose minimum from current and two substring
                    after ignoring ith and kth char
                    '''
                for K in range(i+2,j+1):
                    if(str[i]==str[K]):
                        dp[i][j]=min(dp[i+1][K-1]+dp[K+1][j],dp[i][j])
                
                i+=1
                j+=1

                return dp[0][N]
            

