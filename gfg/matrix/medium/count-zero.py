"""
Given a NxN binary matrix, where each row and column of the matrix is
sorted in ascending order, count number of 0s present in it.

"""
def countZeroes(mat):
    # start from bottom left corner of the matrix
    N=5
    row=N-1
    col=0

    # stores number of zeroes in the matrix
    count=0

    while (col<N):
        # move untill you find a zero
        while(mat[row][col]):
            # if zero is not found in current column, we are done
            if (row<0):
                return count
            row=row-1
        
        # add 0s present in current column to result
        count=count+(row+1)
        # move right to next column
        col=col+1
    
    return count

