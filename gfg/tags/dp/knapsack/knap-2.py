"""
Putting Items in 0/1 knapsack:

Given weights and values of n items, put these items in a knapsack
of capacity W to get the maximum total value in the knapsack. In other words, given
two integer arrays, val[0,..n-1] and wt[0..n-1] represent values and weights associated
with n items respectively. Also given an integer W which represents knapsack capacity,
find out the items such that sum of the weights of those items of a given subset
is smaller than or equal to W.

"""

# Prints the items which are put in a knapsack of capacity W

def printknapSack(W,wt,val,n):
    K=[[0 for w in range(W+1)] for i in range(n+1)]

    # Build table K[][] in bottom  up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    
    # stores the result of knapsack
    res=K[n][W]

    print(res)

    w=W
    for i in range(n,0,-1):
        if res<=0:
            break
        # either the result comes from the top k[i-1][w] or from (val[i-1]+K[i-1][w-wt[i-1]])
        # as in knapsack table. If it comes from the latter one/ it means the item is included
        if res==K[i-1][w]:
            continue
        else:
            print(wt[i-1])
            # since this weight is included its value is deducted
            res=res - val[i-1]
            w=w-wt[i-1]

            

