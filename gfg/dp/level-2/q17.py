# A recursive python program for partition problem

# A utility function that returns true if there is a subset of
# arr[] with sum equal to given sum

def isSubsetSum(arr,n,sum):
    # Base Cases
    if sum==0:
        return True
    
    if n==0 and sum !=0:
        return False
    
    # If last element is greater than sum, then ignore it
    if arr[n-1]> sum:
        return isSubsetSum(arr,n-1,sum)
    # Else check if sum can be obtained by any of the following
    # 1-> including the last element
    # 2-> excluding the last element

    return isSubsetSum(arr,n-1,sum) or isSubsetSum(arr,n-1,sum-arr[n-1])

# Return true if arr[] can be partitioned in two subsets of equal sum,
# otherwise false

def findPartion(arr,n):
    # Calculate sum of the elements in array
    sum=0

    for i in range(0,n):
        sum+=arr[i]
    
    # If sum is odd, there cannot be two subsets with equal sum
    if sum%2!=0:
        return False
    
    # Find if there is subset with sum equal to half of total sum
    return isSubsetSum(arr,n,sum//2)

