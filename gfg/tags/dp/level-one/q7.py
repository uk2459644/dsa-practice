"""
Construction of longest increasing subsequence (LIS) and printing
LIS sequence.

Given an array arr[] of size N, the task is to find the length of the
longest increasing subsequence, the longest possible subsequence in which the 
elements of the subsequence are sorted in increasing order.

"""
# Global variable to store the maximum 
global maximum 

# To make use of recursive calls, this function must return two things:
# 1-> Length of LIS ending with element arr[n-1]. We use 
# max_ending_here for this purpose 
# 2-> Overall maximum as the LIS may end with an element before arr[n-1]
# max_ref is used this purpose.
# The value of LIS of full array of size n is stored in *max_ref which is
# our final result. 

def _lis(arr,n):
    # To allow the access of global variable
    global maximum 
    # Base case 
    if n==1:
        return 1
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere=1
    # Recursively get all LIS ending with
    # arr[0],arr[1]..arr[n-2]
    # IF arr[i-1] is smaller than arr[n-1], and max ending with arr[n-1]
    # needs to be updated, then update it
    for i in range(1,n):
        res=_lis(arr,i)
        if arr[i-1]<arr[n-1] and arr[n-1] and res+1>maxEndingHere:
            maxEndingHere=res+1 
    
    # compare maxEndinghere with overall maximum, And update the
    # overall maximum if needed
    maximum=max(maximum,maxEndingHere)
    return maxEndingHere



