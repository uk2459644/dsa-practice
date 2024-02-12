# Python implementation to the print all the
# possible solutions of the 0/1 knapsack problem

INT_MIN=-2147483648

def nextPermutation(nums:list)->None:
    # Do not return anything, modify nums in-place instead
    if sorted(nums,reverse=True)==nums:
        return True
    
    n=len(nums)
    brk_point=-1
    


