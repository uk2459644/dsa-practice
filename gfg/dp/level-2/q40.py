
# Maximum sum increasing subsequence

# maxSumIs() returns the maximum sum of increasing subsequence
# in arr[] of size n

def maxSumIS(arr,n):
    max=0
    msis=[0 for x in range(n)]
    # initialize msis values for all indexes
    for i in range(n):
        msis[i]=arr[i]
    
    # Compute maximum sum values in bottom up manner
    for  i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j] and msis[i]<msis[j]+arr[i]:
                msis[i]=msis[j]+arr[i]

    # pick maximum of all msis values
    for i in range(n):
        if max<msis[i]:
            max=msis[i]
    
    return max


