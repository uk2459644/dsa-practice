
# Python program to find minimum number of jumps
# to reach end

# Returns minimum number of jumps to reach arr[h]
# from arr[l]

import sys

def minJumps(arr,l,h):
    # Base case: when source and destination
    # are same
    if h==l:
        return 0
    
    # When nothing is reachable from the given source
    if arr[l]==0:
        return sys.maxsize
    
    # Traverse through all the points reachable from l
    min=sys.maxsize
    for i in range(l+1,h+1):
        if (i<l+arr[l]+1):
            jumps=minJumps(arr,i,h)
            if (jumps != float('inf') and jumps+1<min):
                min=jumps+1
    
    return min

nli=list(map(int,input().split()))
n=len(nli)

print(minJumps(nli,0,n-1))


