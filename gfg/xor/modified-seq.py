"""
Given an integer array A of size N, and Q queries. In each query,
you are given an integer X. Create a new sequence X^A[i], say sequence B.
For each query find the number of even integers in the modified sequence for
a given value of X.

"""
"""
Naive Approach:

The idea is to generate the new sequence B for each query and store it.
Now, traverse through the new sequence and count the number of even
numbers.

"""

# Function to return the query answer
def calculate(A,N,X):
    # Initialize even count to zero
    evenCount = 0
    # Traverse the given sequence
    for i in A:
        # Calculate the new sequence XOR
        B=i^X

        # Ignore if the new number is odd
        if B&1:
            continue 
        else:
            evenCount+=1 
        
    return evenCount


