# Program to find minimum step to delete a string 

def helper(str,si,ei,dp):
    # if the string is empty need no operation
    if si > ei :
        return 0
    
    # string length one need one operation
    if ei-si+1 == 1:
        return 1 
    # if already calculated 
    if dp[si][ei]!=-1:
        return dp[si][ei]
    # to consider three operations 
    op1=1e9
    op2=1e9
    op3=1e9

    # delete first char and call on the smaller subproblem
    op1=1+helper(str,si+1,ei,dp)
    # first two characters are same 
    if str[si]==str[si+1]:
        op2=1+helper(str,si+2,ei,dp)
    
    # found another index where the character is saame as si-th character
    for i in range(si+2,ei+1):
        if str[si]==str[i]:
            op3=min(op3,helper(str,si+1,i-1,dp)+helper(str,i+1,ei,dp))
    dp[si][ei]=min(op1,op2,op3)
    return dp[si][ei]

