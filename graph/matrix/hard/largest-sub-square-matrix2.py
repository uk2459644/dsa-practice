"""
Space Optimized Solution: 

In order to compute an etry at any position in the matrix we only need the
current row and the previous row.

"""
R=6
C=5

def printMaxSubSquare(M):
    global R,C
    Max=0

    # set all elements of S to 0 first
    S=[[0 for col in range(C)] for row in range(2)]
    # construct the entries
    for i in range(R):
        for j in range(C):
            # compute the entries at the current position
            Entrie=M[i][j]

            if (Entrie):
                if (j):
                    Entrie=1+min(S[1][j-1],min(S[0][j-1],S[1][j]))
            
            S[0][j]=S[1][j]
            S[1][j]=Entrie

            Max=max(Max,Entrie)
            