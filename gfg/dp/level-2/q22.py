
# Recursive python program for counting coin change problem

# return the count of ways we can sum coins[0...n-1] coins to get sum

def count(coins,n,sum):
    # if sum is 0 then there is 1 solution
    # do not include any coin
    if sum==0:
        return 1
    
    # if sum is less than 0 then no solution exists
    if sum <0:
        return 0
    
    # count is sum of solutions
    # 1-> including coins[n-1] 2-> excluding coins[n-1]

    return count(coins,n-1,sum)+count(coins,n-1,sum-coins[n-1])

