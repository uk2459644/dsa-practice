# Subset sum problem

# A recursive solution for subset sum problem

# Return true if there is a subset of set[] with
# sum equal to given sum

def isSubsetSum(set,n,sum):
    # Base case
    if sum==0:
        return True
    
    if n==0:
        return False
    # If last element is greater than sum, then ignore it
    if set[n-1]>sum:
        return isSubsetSum(set,n-1,sum)
    
    # Else check if sum can be obtained by any of the following
    # 1-> Including the last element
    # 2-> Excluding the last element

    return isSubsetSum(set,n-1,sum) or isSubsetSum(set,n-1,sum-set[n-1])


