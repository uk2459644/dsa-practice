"""
Partition problem :

The partition problem is to determine whether a given set can be partitioned
into two subets such that the sum of elements in both subsets is the same.

The following are two main steps to solve this problem: 
- Calculate the sum of the array. If the sum is odd, there can not be two subsets
  with an equal sum, so return false.

- If the sum of the array elements is even, calculate sum/2 and find a subset
  of the array with a sum equal to sum/2.

"""
"""
Follow the below steps to solve the problem: 
- First check if the sum of the elements is even or not. 
- After checking, call the recursive function isSubsetSum with parameter
  as input array, array size, and sum/2 
  - If the sum is equal to zero then return true (Base case)
  - If n is equal to zero and sum is not equal to 0 then return false.
  - Check if the value of the last element is greater than the remaining sum
    then call this function again by removing the last element.

"""

"""
A utility function that returns true if there is a subset of arr[]
with sum equal to given sum.

"""

def isSubsetSum(arr,n,sum):
    # base case
    if sum==0:
        return True
    
    if n==0 and sum!=0:
        return False
    
    # If last element is greater than sum, then ignore it
    if arr[n-1]>sum:
        return isSubsetSum(arr,n-1,sum)
    
    # else, check if sum can be obtained by any of the following
    # including the last element, excluding the last element
    return isSubsetSum(arr,n-1,sum) or isSubsetSum(arr,n-1,sum-arr[n-1])

def findPartion(arr,n):
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    
    # if sum is odd, there cannot be  two subsets with equal sum
    if sum%2!=0:
        return False
    # Find if there is subset with sum equal to half of total sum
    return isSubsetSum(arr,n,sum//2)



