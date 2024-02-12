"""
Given two arrays, find length of the longest common increasing subsequence
[LCIS] and print one of such sequence may exist
.
"""

# Returns the length and the LCIS of two arrays arr1[0..,n-1] and arr2[0..m-1]

def LCIS(arr1,n,arr2,m):
    # table[j] is going to store length of LCIS ending with arr2[j].
    # we initialize it as 0,
    table=[0]*m
    for j in range(m):
        table[j]=0
    
    # traverse all elements of arr1[]
    for i in range(n):
        # initialize current length of LCIS
        current=0
        # For each element of arr1[],
        # traverse all element of arr2[]
        for j in range(m):
            # if both the array have same elements, note that 
            # we don't break the loop here
            if (arr1[i]==arr2[j]):
                if(current+1 > table[j]):
                    table[j]=current+1
            
            # Now seek for previous smaller common element 
            # for current element of arr1
            if (arr1[i]>arr2[j]):
                if (table[j]>current):
                    current=table[j]
    
    result=0
    for i in range(m):
        if (table[i]>result):
            result=table[i]
    
    return result

        

