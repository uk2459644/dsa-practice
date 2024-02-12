"""
Given a string containing characters as integers only.
We need to delete all characters of this string in a minimum number of
steps wherein one step we can delete the substring which is a palindrome.
After deleting a substring remaining parts are concatenated.
"""

"""
Approach 1: Recursion + Memoization :

We can use recursion to solve the problem and memoization to optimize it.
If the size of the string is one then only one operation is needed. If the first two
characters are same then call on the subproblem with i+2 as an index and add 1 to the 
returned answer. 

"""

# Program to find minimum step to dellete a string

def helper(str,si,ei,dp):
    # If the string is empty need no operation
    if si>ei:
        return 0
    
    if ei-si +1 ==1:
        return 1
    # If already calculated
    if dp[si][ei]!=-1:
        return dp[si][ei]
    
    # to consider three options
    op1=1e9
    op2=1e9
    op3=1e9

    # delete first char and call
    # on the smaller subproblem
    op1=1+helper(str,si+1,ei+1,dp)

    # First two characters are same
    if str[si]==str[si+1]:
        op2=1+helper(str,si+2,ei,dp)
    
    # found another index where the character is same as si-th character
    for i in range(si+2,ei+1):
        if str[si]==str[i]:
            op3=min(op3,helper(str,si+1,i-1,dp))
    
    # return the minimum b/w three options
    dp[si][ei]=min(op1,op2,op3)

    return dp[si][ei]

"""
Approach 2:
"""

def minStepToDeleteString(str):
    N=len(str)
    # declare dp array and initialize it with 0s
    dp=[[0 for x in range(N+1)] for y in range(N+1)]

    # loop for substring length we are considering 
    for l in range(1,N+1):
        # loop with two variables i and j, denoting starting and ending
        # of substring
        i=0
        j=l-1

        while j<N:
            # if substring length is 1, then 1 step will be needed
            if (l==1):
                dp[i][j]=1
            else:
                # delete the ith char individually and asign result
                # for subproblem (i+1,j)
                dp[i][j]=1+dp[i+1][j]
                # if current and next char are same, choose min from
                # current and subproblem (i+2,j)
                if str[i]==str[i+1]:
                    dp[i][j]=min(1+dp[i+2][j],dp[i][j])
                
                # loop over all right characters and suppose kth char is 
                # same as ith character then choose minimum from current and two
                # substring after ignoring ith and kth char.

                for k in range(i+2,j+1):
                    if(str[i]==str[k]):
                        dp[i][j]=min(dp[i+1][k-1]+dp[k+1][j],dp[i][j])
                        

