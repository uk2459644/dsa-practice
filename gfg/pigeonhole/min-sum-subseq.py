"""
Given an array arr[] of positive integers. The task is to find minimum
sum subsequence from the array such that at least one value among all groups
of four consecutive elements is picked.

"""
"""
Returns sum of minimum sum subsequence such that one of every four consecutive
element is picked from arr[].
"""
def minSum(arr,n):
    # dp[i] is goinng to store minimum sum subsequence of arr[0..i] such that
    # arr[i] is part of the solution. Note that this may not be the best solution
    # for subarray arr[0..i]
    dp=[0]*n
    # if there is single value, we get the minimum sum equal to arr[0]
    if (n==1):
        return arr[0]
    # if there are two values we get the minimum sum equal to the minimum
    # of two values 
    if (n==2):
        return min(arr[0],arr[1])
    # if there are three values, return minimum of three elements of array
    if (n==3):
        return min(arr[0],arr[1],arr[2])
    
    if (n==4):
        return min(arr[0],arr[1],arr[2],arr[3])
    
    dp[0]=arr[0]
    dp[1]=arr[1]
    dp[2]=arr[2]
    dp[3]=arr[3]

    for i in range(4,n):
        dp[i]=arr[i]+min(dp[i-1],dp[i-2],dp[i-3],dp[i-4])
    
    return min(dp[n-1],dp[n-2],dp[n-3],dp[n-4])

# function to calculate min sum using dp 
def minSum(ar,n):
    # if elements are less than or equal to 4 
    if (n<=4):
        return min(ar)
    
    sum[0]=ar[0]
    sum[1]=ar[1]
    sum[2]=ar[2]
    sum[3]=ar[3]

    # compute sum[] for all rest elements 
    for i in range(4,n):
        sum[i]=ar[i]+min(sum[i-4:i])
    
    return min(sum[n-4:n])

