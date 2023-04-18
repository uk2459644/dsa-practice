"""
Precompute the number of segment used by digits
from0 to 9 and store it. Now for each element of the
array sum the number of segment used by each digit.
Then find the element which is using the minimum number of segements.
"""

seg=[6,2,5,5,4,5,6,3,7,6]

# Return the number of segments used by x.

def computeSegment(x):
    if (x==0):
        return seg[0]
    
    count=0
    # Finding sum of the segment
    # used by each digit of a number
    while(x):
        count+=seg[x%10]
        x=x//10 
    
    return count

# function to return minimum sum index
def elementMinSegment(arr,n):
    # initialising the minimum 
    # segment and minimum number index 
    minseg=computeSegment(arr[0])
    minindex=0

    for i in range(1,n):
        temp=computeSegment(arr[i])

        if (temp<minseg):
            minseg=temp
            minindex=i
    
    return arr[minindex]
