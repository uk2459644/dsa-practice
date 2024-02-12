# Interleaing string characters

"""
Approach: 

1. If the first character of C matches the first character of A, we move
   one character ahead in A and C and recursively check

2. If the first character of C matches the first character of B, we move one
   character ahead in B and C and recursively check

"""
def isInterleaved(A,B,C):
    # Base case: if all strings are empty
    if not A and not B and not C:
        return True
    
    # If C is empty and any of the two string is not
    if not C:
        return False
    
    # If first character of C matches the first character of A then 
    # recursively check the rest of A and C
    if A and C[0]==A[0]:
        return isInterleaved(A[1:],B,C[1:])
    
    # If the first character of C matches the first character of B
    # then recursively check the rest of B and C
    if B and C[0]==B[0]:
        return isInterleaved(A,B[1:],C[1:])
    
    # If none of the above conditions are met, then C cannot be interleaved
    # From A and B
    return False


