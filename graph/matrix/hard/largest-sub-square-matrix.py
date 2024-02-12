"""
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

Algorithm:
Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct
an auxiliary size matrix S[][] in which each entry S[i][j] represents the size of
the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost
and bottom-most entry in sub-matrix.

1. Construct a sum matrix S[R][C] for the given M[R][C].
   a- Copy first row and first column as it is from M[][] to S[][]
   b- For other entries, use following expressions to construct S[][]
      
      if M[i][j] is 1 then
         S[i][j]=min(S[i][j-1],S[i-1][j],S[i-1][j-1])+1
      Else if M[i][j] is 0:
          S[i][j]=0

2. Find the maximum entry in S[R][C]
3. Using the value and coordinates of maximum entry in S[i],
   print sub-matrix of M[][].

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
    
    # here we have the first row and first column.
    # update other entries
    for i in range(1,R):
        for j in range(1,C):
            if (M[i][j]==1):
                S[i][j]=min(S[i][j-1],S[i-1][j],S[i-1][j-1])+1
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
                
