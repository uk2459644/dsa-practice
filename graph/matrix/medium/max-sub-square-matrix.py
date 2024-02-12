"""
Let the given binary matrix be M[R][C]. The idea of the algorithm is 
to construct an auxiliary size matrix S[][] in which each entry S[i][j]
represents the size of the square sub-matrix with all 1s including M[i][j]
where M[i][j] is the rightmost and bottom-most entry in sub-matrix.

"""
def printMaxSubSquare(M):
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
    for i in range(1,R):
        for j in range(1,C):
            if (M[i][j]==1):
                S[i][j]=min(S[i-1][j],S[i][j-1],S[i-1][j-1])+1
            else:
                S[i][j]=0
    
    # find the maximum entry and indices of maximum entry in S[][]
    max_of_s=S[0][0]
    max_i=0
    max_j=0
    for i in range(R):
        for j in range(C):
            if (max_of_s<S[i][j]):
                max_of_s=S[i][j]
                max_i=i
                max_j=j
    
    print("MAximum size sub-matrix is: ")
    for i in range(max_i,max_i-max_of_s,-1):
        for j in range(max_j,max_j-max_of_s,-1):
            print(M[i][j],end=" ")

