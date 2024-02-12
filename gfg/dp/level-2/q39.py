"""

A Dynamic programming based python program to check whether a string C
is an interleaving of two other strings A and B.

The main function that returns true if C is an interleaving of A and B, otherwise
false

"""
def isInterleaved(A,B,C):
    # find length of the two strings
    M=len(A)
    N=len(B)
    # Let us create a 2D table to store solutions of subproblems. C[i][j]
    # will be true if C[0..i+j-1] is an interleaving of A[0..i-1] and B[0..j-1]
    # Initialize all values as false

    IL=[[False]*(N+1) for i in range(M+1)]

    # C can be an interleaving of A and B only if sum of A and B is equal
    # to length of C
    if ((M+N)!=len(C)):
        return False
    
    # Process all characters of A and B 
    for i in range(0,M+1):
        for j in range(0,N+1):
            # two empty strinngs have an empty string as interleaving
            if i==0 and j==0:
                IL[i][j]=True
            # A is empty
            elif i==0:
                if B[j-1]==C[j-1]:
                    IL[i][j]=IL[i][j-1]
            # B is empty
            elif j==0:
                if A[i-1]==C[i-1]:
                    IL[i][j]=IL[i-1][j]
            # Current character of C matches with current character of A,
            # but doesn't match with current character of B
            elif A[i-1]==C[i+j-1] and B[j-1]!=C[i+j-1]:
                IL[i][j]=IL[i-1][j]
            # Current character of C matches with
            # current character of B, but doesn't match
            # with current character of A
            elif (A[i - 1] != C[i + j - 1] and
                  B[j - 1] == C[i + j - 1]):
                IL[i][j] = IL[i][j - 1]
 
            # Current character of C matches with
            # that of both A and B
            elif (A[i - 1] == C[i + j - 1] and
                  B[j - 1] == C[i + j - 1]):
                IL[i][j] = (IL[i - 1][j] or IL[i][j - 1])

    return IL[M][N]

