# A recursive python program for partition problem

# A utility function that returns true if there is a subset of 
# arr[] with sum equal to given sum

def isSubsetSum(arr,n,sum):
    # Base case
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False
    
    # If last element is greater than sum, then ignore it
    if arr[n-1]>sum:
        return isSubsetSum(arr,n-1,sum)
    # else check if sum can be obtained by any of the following
    # 1 including the last element
    # 2 excluding the last element
    return isSubsetSum(arr,n-1,sum) or isSubsetSum(arr,n-1,sum-arr[n-1])

