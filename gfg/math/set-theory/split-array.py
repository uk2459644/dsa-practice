"""
Given an array arr[] consisting of N distinct integers, the task is to find
the minimum number of times the array needs to be split into two subsets such
that elements of each pair are present into two different subsets at least once.

"""

def minimumNoOfWay(arr,n):
    min_no_of_ways=n//2

    if (n%2==0):
        min_no_of_ways=n//2
    else:
        min_no_of_ways=n//2+1
    
    return min_no_of_ways

