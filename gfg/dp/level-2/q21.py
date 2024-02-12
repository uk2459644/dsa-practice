
# A memoization solution for rod cutting problem

# Returns the best obtainable price for a rod of length n and price[]
# as prices of different places

def cutRod(price,index,n,dp):

    # base case
    if index==0:
        return n*price[0]
    
    if dp[index][n]!=-1:
        return dp[index][n]
    
    # At any index we have 2 options either cut the rod of this
    # length or not cut it
    notCut=cutRod(price,index-1,n,dp)
    cut=-5
    rod_length=index+1
    



