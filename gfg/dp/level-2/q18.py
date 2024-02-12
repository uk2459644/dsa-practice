# Partition problem using memoization

# A utility function that returns true if there is a subset of arr[]
# with sum equal to given sum

def isSubsetSum(arr,n,sum,dp):
    # Base Cases
    if sum==0:
        return True
    
    if n==0 and sum !=0:
        return False
    
    # return solved subproblem
    if dp[n][sum] != -1:
        return dp[n][sum]
    
    # If last element is greater than sum, then ignore it
    if arr[n-1]>sum:
        return isSubsetSum(arr,n-1,sum,dp)
    # Else, check if sum can be obtained by any of the following
    # 1-> including the last element 
    # 2-> excluding the last element

    # also store the subproblem in dp matrix
    dp[n][sum]=isSubsetSum(arr,n-1,sum,dp) or isSubsetSum(arr,n-1,sum-arr[n-1],dp)

    return dp[n][sum]

# Return true if arr[] can be partitioned in two subsets of equal sum,
# otherwise false

def findPartition(arr,n):
    # Calculate sum of the element in array
    sum=0
    for i in range(n):
        sum+=arr[i]
    
    # If sum is odd, there cannot be two subsets with equal sum
    if sum%2!=0:
        return False
    
    # To store overlapping subproblems
    dp=[[-1]*(sum+1) for i in range(n+1)]
    # Find if there is subset with sum equal to half of total sum
    return isSubsetSum(arr,n,sum//2,dp)


