"""
Memoization for knap-9

As the above recursive solution has overlapping subproblem so we can
declare a 2-D array to save the values for different states of the recursive
function instead of solving them more than once.

"""
"""
Follow the below steps to solve the problem: 
- Declare a 2-D array of size N+1 X sum+1 
- Call the recursive function with parameters as input array, size, sum, and dp array
- In this recursive function 
  - If the sum is equal to zero then return true (Base case)
  - If n is equal to 0 and sum is not equal to zero then return false (Base case)
  - If the value of this subproblem is already calculated then return the answer from dp array
  - Else calculate the answer for this subproblem using the recursive formula in the above approach
  and save the answer in the dp array
  - return the answer as true or false

"""
# A utility function that returns true if there is a subset of arr[] with
# sum equal to given sum

def isSubsetSum(arr,n,sum,dp):
    # Base case
    if (sum==0):
        return True
    
    if (n==0 and sum!=0):
        return False
    
    # return solved subproblem
    if (dp[n][sum]!=-1):
        return dp[n][sum]
    
    # If last element is greater than sum, then ignore it
    if (arr[n-1]>sum):
        return isSubsetSum(arr,n-1,sum,dp)
    
    # else, check if sum can be obtained by any of the following
    # 1- including the last element
    # 2- excluding the last element
    # also store the subproblem in dp matrix
    dp[n][sum]=isSubsetSum(arr,n-1,sum,dp) or isSubsetSum(arr,n-1,sum-arr[n-1],dp)

    return dp[n][sum]

# Returns True if arr[] can be partitioned in two subset of equal sum, otherwise false

def findPartion(arr,n):
    # Calculate sum of the elements in array
    sum=0
    for i in range(n):
        sum+=arr[i]
    
    # If sum is odd, there cannot be two subsets with equal sum
    if (sum%2!=0):
        return False
    
    # To store overlapping subproblems
    dp=[[-1]*(sum+1) for i in range(n+1)]

    # Find if there is subset with sum equal to half of the total sum
    return isSubsetSum(arr,n,sum//2,dp)

