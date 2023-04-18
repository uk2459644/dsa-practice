# python code to implement the above approach
# function to find the 
# minimum number of jumps required
def minimizeJumps(arr):
    n=len(arr)
    # initialize a map for mapping element with
    # indices of all similar value occurences in array
    unmap={}
    # mapping element with indices
    for i in range(n):
        if arr[i] in unmap:
            unmap.get(arr[i]).append(i)
        else:
            unmap.update({arr[i]:[i]})
    q=[]
    visited=[False]*n
    # push starting element into queue and
    # mark it visited
    q.append(0)
    visited[0]=True
    # initialize a variable count for counting the
    # minimum number , number of valid jump to reach at last index
    count=0
    # do while queue size is greater than 0
    while (len(q)>0):
        size=len(q)
        # iterate on all the 
        # elements of queue
        for i in range(size):
            curr=q[0]
            q.pop(0)
            