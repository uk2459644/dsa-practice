# A Naive recursive program to find minimum number of insertion
# needed to make a string palindrome

import sys

# Recursive function to find minimum number of insertions
def findMinInsertions(str,l,h):
    # Base cases
    if(l>h):
        return sys.maxsize
    
    if l==h:
        return 0
    
    if l==h-1:
        return 0 if str[l]==str[h] else 1
    
    # Check if the first and last characters are same. On the
    # basis of the comparison result, decide which subproblem to call

    if str[l]==str[h]:
        return findMinInsertions(str,l+1,h-1)
    else:
        return findMinInsertions(min(findMinInsertions(str,l,h-1),findMinInsertions(str,l+1,h))+1)
    


