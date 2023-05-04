"""
Given a binary matrix, find out the matrix size square sub-matrix with all 1s.

Algorithm:
LEt the given binary matrix be M[R][C]. The idea of the algorithm is to
construct and auxiliary size matrix S[][] in which each entry S[i][j] represents
the size of the square sub-matrix with all 1s including M[i][j] where M[i][j]
is the rightmost and bottom-most entry in sub-matrix.
"""
def printMAxSubSquare(M):
    R=len(M)
    C=len(M[0])

    S=[]
    for i in range(R):
        temp=[]
        for j in range(C):
            if i==0 or j==0:
                temp+=M[i][j]
            else:
                temp+=0
        S+=temp
    
    # update other entries
    


