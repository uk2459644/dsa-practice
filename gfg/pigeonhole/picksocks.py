"""
Given an array arr[] consisting of N integers such that arr[i]
representing the number of socks of the color i and an integer K,
the task is to find the minimum number of socks required to be picked to get
at least k pairs of socks of the same color.

"""
"""
Approach: The given problem can be solved on the following observations:

- According to Pigeonhole's Principle, in the worst-case scenario if N socks
  of different colors have been picked then the next pick will form a matching
  pair of socks.

- Suppose one has picked N socks of different colors then, for each (k-1) pairs
  one will need to pick two socks, one for forming a pair and another for maintaining
  N socks of all different colors, and for the last pair, there is only need to pick a single sock of any
  color available.

"""
# Function to count the minimum number of socks to be picked

def findMin(arr,N,k):
    # Stores the total count of pairs of socks 
    pairs=0
    # find the total count of pairs 
    for i  in range(N):
        pairs+=arr[i]/2 
    
    # If k is greater than pairs 
    if (k>pairs):
        return -1 
    else:
        return 2*k+N-1 
    
