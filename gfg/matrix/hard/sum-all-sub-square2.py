"""
Tricky Solution: 

The idea is to preprocess the given square matrix. In the preprocessing
step, calculate sum of all vertical strips of size kx1 in a temporary square
matrix stripSum[][]. Once we have sum of all vertical strips, we can calculate sum of first
sub-square in a row as sum of first k strips in that row, and for remaining sub-squares, we can calculate
sum in O(1) time by removing leftmost strip of previous subsquare and adding rightmost strip of new square.


"""
def printSumTricky(mat,k):
    global n 

    # k must be smaller than or equal to n
    if k>n :
        return
    
    # Preprocessing: To store sums of all strips of size kx1
    stripSum=[[None]*n for i in range(n)]

    # Go column by column
    for j in range(n):
        # Calculate sum of first kx1 rectangle in this column
        sum=0
        for i in range(k):
            sum+=mat[i][j]
        
        stripSum[0][j]=sum

        # calculate sum of remaining rectangles 
        for i in range(1,n-k+1):
            sum+=(mat[i+k-1][j]-mat[i-1][j])
            stripSum[i][j]=sum
        
         # 2: CALCULATE SUM of Sub-Squares
    # using stripSum[][]
    for i in range(n - k + 1):
         
        # Calculate and print sum of first
        # subsquare in this row
        Sum = 0
        for j in range(k):
            Sum += stripSum[i][j]
        print(Sum, end = " ")
 
        # Calculate sum of remaining squares
        # in current row by removing the leftmost 
        # strip of previous sub-square and adding
        # a new strip
        for j in range(1, n - k + 1):
            Sum += (stripSum[i][j + k - 1] -
                    stripSum[i][j - 1])
            print(Sum, end = " ")
 
