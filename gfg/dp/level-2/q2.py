# Subset sum problem using Memoization

# taking the matrix as globally
tab=[[-1 for i in range(2000)]for j in range(2000)]

# Check if possible subset with given sum is possible
# or not

def subsetSum(a,n,sum):
    # If the sum is zero it means we got our expected sum
    if sum==0:
        return 1
    
    if n<=0:
        return 0
    
    # If the value is not -1 it means it already call the function
    # with the same value, it will save us, from the repetition.
    if (tab[n-1][sum]!=-1):
        return tab[n-1][sum]
    
    # If the value of a[n-1] is greater than the sum. we call for the
    # next value
    if (a[n-1]>sum):
        tab[n-1][sum]=subsetSum(a,n-1,sum)
        return tab[n-1][sum]
    else:
        # Here we do two calls because we don't know which value will
        # full fill our criteria that's why we doing two calls
        tab[n-1][sum]=subsetSum(a,n-1,sum)

        return tab[n-1][sum] or subsetSum(a,n-1,sum-a[n-1])
    
    

