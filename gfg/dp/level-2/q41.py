
# Minimum number of jumps to reach the end using recursion:

"""
Follow the steps mentioned below to implement the idea:

- Create a recursive function
- In each recursive call get all the reachable nodes from that index.
- For each of the index call the recursive function.
- Find the minimum number of jumps to reach the end from current index.
- Return the minimum number of jumps from the recursive call.

"""

# Return minimum number of jumps to reach arr[h] from arr[l]

def minJumps(arr,l,h):
    # Base case : when source and  destination are same
    if h==l:
        return 0
    
    # When nothing is reachable from the given source
    if arr[l]==0:
        return float('inf')
    
    # Traverse through all the points reachable from arr[l].
    # Recursively get the  minimum number of jumps needed to reach 
    # arr[h] from these reachable points
    min=float('inf')
    for i in range(l+1,h+1):
        



