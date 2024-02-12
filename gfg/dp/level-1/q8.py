# Maximum product cutting 
# Given a rope of length n meters, cut the rope in different parts of
# integer lengths in a way that maximizes product of length of all
# parts. 



# The main function that returns maximum product
# obtainable from a rope of length n

def maxProd(n):
    # Base case
    if n==0 or n==1:
        return 0
    
    # Make a cut at different places and take the
    # maximum of all
    max_val=0
    for i in range(1,n-1):
        max_val=max(max_val,max(i*(n-i),maxProd(n-i)*i))
    
    # Return the maximum of all values
    return max_val
