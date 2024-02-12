"""
Given an array arr[] consisting of N integers and an integer K, the task
is to select some non-adjacent array elements with the maximum possible sum
not exceeding K.

"""

"""
Naive Approach: The simplest approach is to recursively generate all possible
subsets of the given array and for each subset, check if it does not contain a
adjacent elements and has the sum not exceeding K. Among all subsets for which
the above condition is found to be true, print.

"""
# Function to find the maximum sum not exceeding K possible by selecting
# a subset of non-adjacent elements

def maxSum(a,n,k):
    # Base case 
    if (n<=0):
        return 0
    
    # Not selecting current element
    option=maxSum(a,n-1,k)
    # If selecting current element is possible
    if  k>=a[n-1]:
        option=max(option,a[n-1]+maxSum(a,n-2,k-a[n-1]))
    
    # return answer
    return option
