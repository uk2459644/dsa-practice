"""
Given weights and profit of N items, put these item in a knapsack
of capacity W. The task is to print all possible solutions to the problem
in such a way that there are no remaining items left whose weight is less
than the remaining capacity of the knapsack. Also, compute the maximum profit.

"""
"""
Approach: The idea is to make pairs for the weight and the profit of the item
and then try out all permutations of the array and including the weights until their
is no such item whose weight is less than the remaining capacity of knapsack.
Meanwhile after including an item increment the profit for that solution
by the profit of that item.

"""

# The possible solutions 

INT_MIN=-2147483648

def nextPermutation(nums:list)->None:
    "Do nto return anything, modify nums in place instead"
    if sorted(nums,reverse=True)==nums:
        return None
    
    n=len(nums)
    brk_point=-1
    for pos in range(n-1,0,-1):
            if nums[pos]>nums[pos-1]:
                brk_point=pos
                break
            else:
                nums.sort()
                return
    replace_with=-1
    for j in range(brk_point,n):
        if nums[j]>nums[brk_point-1]:
            replace_with=j
        else:
            break
    nums[replace_with],nums[brk_point-1]=nums[brk_point-1],nums[replace_with]
    nums[brk_point:]=sorted(nums[brk_point:])
    return nums

# Function to find the all the possible solutions of the knapsack problme

def knapSack(W,wt,val,n):
    #  Mapping weight with profits
    umap=dict()
    set_sol=set()
    # making pairs and inserting the map
    for i in range(n):
        umap[wt[i]]=val[i]
    result=INT_MIN
    remining_weight=0

    sum=0
    # loop to iterate over all the possible permutation of array
    while True:
        sum=0
        # initially bag will be empty
        remining_weight=W
        possible=[]
        # loop to fill up the bag untill there is no weight less
        # than remaining weight of the knapsack
        for i in range(n):
            if wt[i]<=remining_weight:
                

