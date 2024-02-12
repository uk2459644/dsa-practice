"""
Space Optimized Iterative Dynamic Programming

Approach:

* As all elements are available as many times as needed, so there is not 
  need to save values for previous rows, the values from the same row
  can be used

* So a 1-D array can be used to save previous results.

* Create an array, dp of size M, where dp[i] stores the maximum number of sorted
  arrays of size i that can be formed from numbers in the range

"""

def countSortedArrays(n,m):
    # create an array of size m+1
    dp=[0 for _ in range(m+1)]

    dp[0]=1

    # fill the dp tables

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[j]=dp[j-1]+dp[j]
    
    return dp[m]


