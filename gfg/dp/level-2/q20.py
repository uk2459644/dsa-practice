# A recursive solution for rod cutting problem

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different prices

def cutRod(price,index,n):
    # base case
    if index==0:
        return n*price[0]
    
    # At any index we have 2 option either cut
    # the rod of this length or not cut it
    notCut=cutRod(price,index-1,n)
    cut=float("-inf")
    rod_length=index+1

    if rod_length<=n:
        cut=price[index]+cutRod(price,index,n-rod_length)

    return max(notCut,cut)



