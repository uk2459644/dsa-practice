"""
Power Set: Power set P(s) of a set S is the set of all subsets of S.

If S has n elements in it then P(s) will have 2^n elements.

Method 1: 
For a given set[] S, the power set can be found by generating all binary
numbers between 0 to 2^n-1. where n is the size of the set.

For example, for the set S{x,y,z}, generate all binary numbers from 0 to 2^3-1
and for each generated number, the corresponding set can be found by considering
set bits in the number.
"""
import math

def printPowerSet(set,set_size):
    # set_size of power set of a set
    # with set_size n is (2**n-1)
    pow_set_size=(int)(math.pow(2,set_size))
    counter=0
    j=0
    for counter in range(0,pow_set_size):
        for j in range(0,set_size):
            if((counter & (1<<j))>0):
                print(set[j],end="")

"""
Method 2: (sorted by cardinality)

In auxiliary array of bool set all elements to 0. That represent an empty
set. Set first element of auxiliary arraay to 1 and generate all permutations
to produce all subsets with one element. Then set the second element to 1
which will produce all subsets with two elementss, repeat until all elements are
included.

"""

# A function which gives previous permutation of the array
# and returns true if a permutation exists.

def prev_permutation(str):
    # find index of the last element of the string
    n=len(str)-1
    # find largest index i such that str[i-1]>str[i]
    i=n
    while (i>0 and str[i-1]<=str[i]):
        i-=1
        # if string is sorted in ascending order find rightmost element
        # index that is less than str[i-1]
        j=i-1

        while (j+1<=n and str[j+1]<str[i-1]):
            j+=1
        
        temper=str[i-1]
        str[i-1]=str[j]
        str[j]=temper
        
