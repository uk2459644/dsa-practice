
def knapSack(W,wt,val,n):
    # Base case 
    if n==0 or W==0:
        return 0
    # If weight of the nth item is more than knapsack of capacity W,
    # then this item cannot be included in the optimal solution
    if(wt[n-1]>W):
        return knapSack(W,wt,val,n-1)
    
    # Return the maximum of two cases :
    # 1 nth item included 
    # 2 not included
    else:
        return max(val[n-1]+knapSack(W-wt[n-1],wt,val,n-1),knapSack(W,wt,val,n-1))
    

# This is the memoization approach of 0/1 knapsack in python in simple
# we can say recursion + memoization = DP 

W=100
n=100

t=[[-1 for i in range(W+1)] for j in range(n+1)]

def knapsack(wt,val,W,n):
    # base condition 
    if n==0 or W==0:
        return 0
    
    if t[n][W]!=-1:
        return t[n][W]
    
    # Choice diagram code 
    if wt[n-1]<=W:
        t[n][W]=max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return t[n][W]
    elif wt[n-1]>W:
        t[n][W]=knapsack(wt,val,W,n-1)
        return t[n][W]
    
    
    
