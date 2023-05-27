"""
Given NxN binary matrix, find the size of the largest + formed by all 1s.

The idea is to maintain four auxiliary matrices left[][], right[][], top[][],
bottom[][] to store consecutive 1's in every direction. For each cell (i,j) in the 
input matrix, we store below information in these four matrices - 

left(i,j) stores maximum number of consecutives 1's to the left of cell (i,j)
including cell (i,j). 

right(i,j) stores maximum number of consecutive 1's to the right of cell (i,j)
including cell (i,j).

top(i,j) stores maximum number of consecutive 1's at top of cell (i,j)
including cell (i,j)

bottom(i,j) stores maximum number of consecutive 1's at bottom of cell (i,j)
including cell (i,j).

"""

"""
We can use Dynamic Programming to compute the total amount of consecutive
1's in every direction.

if mat(i,j)==1:
   left(i,j)=left(i,j-1)+1
else left(i,j)=0

"""
N=16

def findLargestPlus(mat):
    left=[[0 for x in range(N)] for y in range(N)]
    right=[[0 for x in range(N)] for y in range(N)]
    top=[[0 for x in range(N)] for y in range(N)]
    bottom=[[0 for x in range(N)] for y in range(N)]

    # initialize above four matrix
    for i in range(N):
        # initialize first row of top
        top[0][i]=mat[0][i]
        bottom[N-1][i]=mat[N-1][i]

        left[i][0]=mat[i][0]
        right[i][N-1]=mat[i][N-1]
    
    # fill all cells of above four matrix 
    for i in range(N):
        for j in range(1,N):
            # calculate left matrix (filled left to right)
            if mat[i][j]==1:
                left[i][j]=left[i][j-1]+1
            else:
                left[i][j]=0
            
            # calculate top matrix
            if mat[j][i]==1:
                top[j][i]=top[j-1][i]+1
            else:
                top[j][i]=0
            
            # calculate new value of j to calculate value of bottom(i,j)
            # and right(i,j)
            j=N-1-j 

            if mat[j][i]==1:
                bottom[j][i]=bottom[j+1][i]+1
            else:
                bottom[j][i]=0
            
            # calculate right matrix
            if mat[i][j]==1:
                right[i][j]=right[i][j+1]+1
            else:
                right[i][j]=0
            
            # revert back to old j
            j=N-1-j
    
    n=0
    # compute longest + 
    for i in range(N):
        for j in range(N):
            # find minimum of left
            l=min(min(top[i][j],bottom[i][j]),min(left[i][j],right[i][j]))

            if l>n:
                n=l
    
    if n:
        return 4*(n-1)+1 
    
    return 0