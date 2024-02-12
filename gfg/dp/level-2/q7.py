# A naive python implementation of LIS problem

# Global varaible to store the maximum
global maximum

# To make use of recursive calls, this function must return two things:
# 1-> Length of LIS ending with element arr[n-1]

def _lis(arr,n):
    # To allow the access of global variable
    global maximum
    # Base case
    if n==1:
        return 1
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere=1

    # Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
    # If arr[i-1] is smaller than arr[n-1], and maxending with arr[n-1]
    # needs to be updated, then update it.
    for i in range(1,n):
        res=_lis(arr,i)
        if arr[i-1]<arr[n-1] and res+1>maxEndingHere:
            maxEndingHere=res+1
    # Compare maxEndinghere with overall maximum. And update the overall
    # maximum if needed
    maximum=max(maximum,maxEndingHere)

    return maxEndingHere


