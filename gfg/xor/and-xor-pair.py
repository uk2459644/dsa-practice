"""
Given an integer array arr[] of size N, the task is to count the number
of pairs whose BITWISE AND and BITWISE XOR are equal.

"""
"""
Approach:

The idea behind this approach is that we can use a dictionary to count the
frequency of each element in the array. Then, we can iterate through all possible pairs
of elements and check if their bitwise XOR is equal to their bitwise AND. if it is, we add
the product of their frequencies to a counter. Finally, we return half the value of the
counter since each pair is counted twice.

"""
def countPairs(n,arr):
    # create a dictionary to count the frequency of each element in
    # the array 
    freq = {}
    for i in arr:
        freq[i]=freq.get(i,0)+1 
    
    ans=0
    # Iterate through all possible pairs of elements in the dictionary
    for i in freq.keys():
        for j in freq.keys():
            # check if their bitwise XOR and AND is equal
            if i^j == i&j:
                # add the product of their frequencies to the counter
                if i==j:
                    ans+=freq[i]*(freq[j]-1)
                else:
                    ans+=freq[i]*freq[j]
    
    # Return half the value of the counter since each pair is counted twice
    print(ans//2)
    
