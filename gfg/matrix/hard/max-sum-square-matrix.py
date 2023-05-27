"""
Print maximum sum squre sub matrix of given size

A simple solution is to consider all possible sub-squares pf size kxk
in our input matrix and find the one which has maximum sum. Time complexity of
above solution is O(N2K2).

The idea is to preprocess the given square matrix. In the preprocessing
step, calculate sum of all vertical strips of size kx1 in a temporary square
matrix stripSum[][]. Once we have sum of all vertical strips, we can calculate
sum of first sub-square in a row as sum of first k strips in that row, and for remaining
sub-squares, we can calculate sum in O(1) time by removing the leftmost
strip of previous subsqure and adding the rightmost strip of new square.

"""
# Size of given matrix 
N=5 

def printMaxSumSub(mat,k):
    # k must be smaller than or equal to n
    if k>N:
        return
    
    # To store sum of all strips of size kx1
    stripSum=[[0 for j in range(N)] for i in range(N) ]
    # go column by column
    for j in range(N):
        # calculate sum of first kx1 rectangle in this column
        sum=0
        for i in range(k):
            sum+=mat[i][j]
        
        stripSum[0][j]=sum
        # calculate sum of remaining rectangle
        for i in range(1,N-k+1):
            sum+=(mat[i+k-1][j]-mat[i-1][j])
            stripSum[i][j]=sum
    
    max_sum=-1000000000
    i_ind=0
    j_ind=0
    # 2: Calculate sumof sub-squre using stripSum
    for i in range(N-k+1):
        sum=0
        for j in range(k):
            sum+=stripSum[i][j]
        
        if sum>max_sum:
            max_sum=sum
            i_ind=i
            j_ind=0
            
