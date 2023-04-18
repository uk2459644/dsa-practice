# python code to implement the above approach

m,n=0,0
def isValid(i,j,x,visited,arr,parent):
    # check if we go outside the matrix or 
    # cell(i,j) is visited or absolute
    # difference between consecutive cell
    # is greater than our assumed maximum energy
    # required if true
    # then return false
    if (i<0 or j<0 or i>=m or j>=n or visited[i][j] or abs(arr[i][j]-parent)>x):
        return False
    # check if we reach at bottom-right cell
    # if true , then return true
    if (i==m-1 and j==n-1):
        return True
    # make the current cell(i,j) visited
    visited[i][j]=True
    # make all four direction call and check if any
    # path is valid if true, then return true
    if (isValid(i+1,j,x,visited,arr,arr[i][j])):
        return True
    if (isValid(i-1,j,x,visited,arr,arr[i][j])):
        return True
    if (isValid(i,j+1,x,visited,arr,arr[i][j])):
        return True
    if (isValid(i,j-1,x,visited,arr,arr[i][j])):
        return True
    
    return False

# function to find the minimum value among the 
# maximum adjacent differences

def minimumEnergyPath(arr):
    # initialize a variable start = 0
    # and end = maximum possible
    # energy required
    start,end=0,10000000
    # initialize a variable result
    result=arr[0][0]
    # loop to implement the binary search
    while (start<=end):
        mid=(start+end)//2
        # initialize a visited array of size (m*n)
        visited=[[False for i in range(n)] for j in range(m)]
        # check if mid energy is valid energy required
        # by choosing any path into the matrix if true,
        # update the result and move end to mid -1
        if (isValid(0,0,mid,visited,arr,arr[0][0])):
            result=mid
            end=mid-1
        else:
            start=mid+1
    return result

