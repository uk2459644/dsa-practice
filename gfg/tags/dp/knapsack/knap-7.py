"""
Given the weights and values of n items, the task is to put these items in
a knapsack of capacity W to get the maximum total value in the knapsack, we can repeatedly
put the same item and we can also put a fraction of an item.

"""

"""
Approach: The idea here is to just find the item which has the largest
value to weight ratio. Then fill the whole knapsack with this item only, in
order to maximize the final value of the knapsack.

"""

import sys 

# function to return the maximum required value

def knapSack(W,wt,val,n):
    # maxratio will store the maximum value to weight ratio we can have
    # for any item and maxindex will store the index of that element

    maxratio=-sys.maxsize-1
    maxindex=0
    # find the maximum ratio
    for i in range(n):
        if ((val[i]/wt[i])>maxratio):
            maxratio=(val[i]/wt[i])
            maxindex=i
    
    # The item with the maximum value to weight ratio will be put into
    # the knapsack repeatedly until full
    return (W*maxratio)


