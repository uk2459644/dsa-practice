"""
Given an array of N integers, the task is to find a non-empty subset such that
the sum of elements of the subset is divisible by N. output any such subset
with its size and the indices of elements in the original array if it exists.

"""

def findNonEmptySubset(arr,N):
    # Hash map to store the indices of residue upon
    # taking modulo N of prefixSum
    mp={}

    Sum=0
    for i in range(N):
        # Calculating the residue of prefixSum
        Sum=(Sum+arr[i])%N
        # if the pre[i]%N==0
        if (Sum==0):
            # print size
            print(i+1)
            # print the first i indice
            for j in range(i+1):
                print(j+1,end=" ")
            return 
        
        # if this sum was seen earlier, then the contiguous 
        # subsegment has been found 
        if Sum in mp:
            # print the size of subset 
            print((i-mp[Sum]))
            # print the indices of contiguous subset
            for j in range(mp[Sum]+1,i+1):
                print(j+1,end=" ")
            
            return
        else:
            mp[Sum]=i
            

