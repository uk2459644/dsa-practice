# A recursive program for partition problem

# a utility function that returns true if there is a subset of arr[]
# with sum equal to given sum

def isSubsetSum(arr,n,sum,dp):
    # Base case
    if (sum==0):
        return True
    if n==0 and sum!=0:
        return False
    
    # return solved subproblem
    if (dp[n][sum] !=-1):
        return dp[n][sum]
    
    # If last element is greater than sum, then ignore it
    if (arr[n-1]>sum):
        return isSubsetSum(arr,n-1,sum,dp)
    # else check if sum can be obtained by any of the following
    # a including the last element
    # b excluding the last element
    # also store the subproblem in dp matrix
    dp[n][sum]=isSubsetSum(arr,n-1,sum,dp) or isSubsetSum(arr,n-1,sum-arr[n-1],dp)

    return dp[n][sum]

# Returns true if arr[] can be partitioned in two subsets of equal sum,
# otherwise false

def findPartition(arr,n):
    # calculate sum of the elements in array
    sum=0
    for i in range(n):
        sum+=arr[i]
    
    # If sum is odd, there can not be two subsets with equal sum
    if sum%2 !=0:
        return False
    # To store overlapping subproblems
    dp=[[-1]*(sum+1) for i in range(n+1)]
    
    # Find if there is subset with sum equal to half of total sum
    return isSubsetSum(arr,n,sum//2,dp)


