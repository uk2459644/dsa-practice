"""
Maximum sum rectangle in a 2D

"""
def kadane(arr,start,finish,n):
    # initialize sum, maxSum and
    Sum=0
    maxSum=-9999999999
    i=None

    # just some initial value to check 
    #  for all negative values case
    finish[0]=-1
    
