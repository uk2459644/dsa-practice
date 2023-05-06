"""
Space optimized solution
"""
R=6
C=5

def printMaxSubSquare(M):
    global R,C
    Max=0

    # set all elements of S to 0 first
    S=[[0 for col in range(C)] for row in range(R)]
    # construct the entries
    for i in range(R):
        for j in range(C):
            # compute the entries at the current position
            Entrie=M[i][j]
            if (Entrie):
                if (j):
                    Entrie=1+min(S[1][j-1],min(S[0][j-1],S[1][j]))
            
            # save the last entry and add the new one
            S[0][j]=S[1][j]
            S[1][j]=Entrie
            Max=max(Max,Entrie)

