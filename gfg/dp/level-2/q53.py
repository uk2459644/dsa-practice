"""
Minimum time to finish tasks without skipping two consecutive

The given problem has the following recursive property. Let minTime(i) be
minimum time to finish till i'th task. It can be written as minimum of two
values.

1. Minimum time if i'th task is included in list, let this time be incl(i)
2. Minimum time if i'th task is excluded from result, let this time be excl(i)

minTime(i)=min(excl(i),incl(i))

"""

# arr[] represents time taken by n given tasks
def minTime(arr,n):
    # Corner cases
    if (n<=0): return 0

    # Initialize value for the case when there is only one task in
    # task list
    incl=arr[0] 
    # first task is included
    excl=0
    # first task is excluded
    # Process remaining n-1 tasks
    for i in range(1,n):
        # Time taken if current task is included
        # There are two possibilities
        # (a) Previous task is also included
        # (b) Previous task is not included
        incl_new=arr[i]+min(excl,incl)

        # Time taken when current task is not included. There
        # is only one possibility that previous task is also included
        excl_new=incl

        # Update incl and excl for next iteration
        incl=incl_new
        excl=excl_new
    
    # return minimum of two values for last task
    return min(incl,excl)




