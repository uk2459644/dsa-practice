"""
Given a square matrix mat[][] and a number k. The task is to shift the
first k elements of each row to the right of the matrix.

"""

N=4

def shiftMatrixByk(mat,k):
    if k>N:
        print("Shifting is not possible")
        return
    
    j=0
    while (j<N):
        # print elements from index kk
        for i in range(k,N):
            print(mat[j][i], end="")
        
        # print elements before index k
        for i in range(0,k):
            print(mat[j][i])
        j+=1 
        

