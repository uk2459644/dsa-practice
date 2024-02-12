"""
Given two numbers N and M, the task is to find the number of sorted array
that can be formed of size M using first N natural numbers, if each number
can be taken any number of times.
 
"""
"""
Naive Approach : There are two choices for each number that it can be taken or can
be left. Also, anumber can be taken multiple times.

*Elements that are taken multiple times should be consecutive in the 
array.

*If an element is left and has moved to another element then that element
can not be taken again.

"""
# Function to find the number of m-length sorted arrays possible
# using numbers from the range

def countSortedArray(start,m,size,n):
    # If size becomes equal to m that means an array is found
    if size == m:
        return 1
    
    if start>n:
        return 0
    
    notTaken,taken=0,0
    # include current element, increase size by 1 and remain on the same
    # element as it can be included again
    taken=countSortedArray(start,m,size+1,n)
    # exclude current element
    notTaken=countSortedArray(start+1,m,size,n)

    return taken+notTaken

# another approach 

def countSortedArrays(st,n,m,ans,size):
    # if size becomes equal to m one sorted array is found
    if size==m:
        ans+=1
        return ans
    
    # traverse over the range
    for i in range(st,n+1):
        # find all sorted arrays starting from i
        ans=countSortedArrays(i,n,m,ans,size+1)
    return ans

# Dynamic Programming approach

# function to find the number of m-length sorted arrays possible using
# umbers from the range.

def countSortedArrays(dp,m,n):
    # base case
    if m==0:
        return 1
    if n<=0:
        return 0
    
    # if the result is already computed, return the result of the state

    if dp[m][n] != -1:
        return dp[m][n]
    
    taken,notTaken=0,0

    # Include current element, decrease size by 1 and remain on the same element
    # as it can be taken again
    taken=countSortedArrays(dp,m-1,n)

    # if element is not taaken
    notTaken=countSortedArrays(dp,m,n-1)

    # store the result and return it
    dp[m][n]=taken+notTaken

    return dp[m][n]
