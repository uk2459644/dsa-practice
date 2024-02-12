"""
Minimum steps to delete a string after repeated deletion of palindrome
substring

Given a string containing characters as integers only.
We need to delete all characters of this string in a minimum number
of steps wherein on step we can delete the substring which is a palindrome.

After deleting a substring remaining parts are concatenated.

"""

# Recursion + Memoization :

# Python program to find minimum step to delete a string
def helper(str,si,ei,dp):
    # If the string is empty 
    # need no operation
    if si > ei :
        return 0
    # string length one need one operation
    if ei-si+1 == 1:
        return 1
    
    # IF already calculated 
    if dp[si][ei] != -1:
        return dp[si][ei]
    

