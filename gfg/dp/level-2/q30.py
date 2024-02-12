"""
The solution is to try dropping an egg from every floor(from 1 to k)
and recursively calculate the minimum number of droppings needed in the
worst case. 

The floor which gives the minimum value in the worst case is going to
be part of the solution.

In the following solutions, we return the minimum number of trials in 
the worst case;
these solutions can be easiliy modified to print
the floor numbers of every trial also.

"""
import sys 

# Function to get minimum number of trials needed in worst case with n eggs
# and k floors

def eggDrop(n,k):
    # If there are no floors, then no trials needed. Or if there is one 
    # floor , one trial needed
    if k==1 or k==0:
        return k
    # We need k trials for one egg and k floors
    if n==1:
        return k
    
    min=sys.maxsize
    # consider all droppings from 1st floor to kth floor and return the
    # minimum of these values plus 1
    for x in range(1,k+1):
        res=max(eggDrop(n-1,x-1),eggDrop(n,k-x))

        if res<min:
            min=res
    
    return min+1



