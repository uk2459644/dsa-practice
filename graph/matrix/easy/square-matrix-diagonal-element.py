"""
You have given an integer with odd dimensions.
Find the square of the diagonal elemetns on both sides.

"""
def diagonalsquare(mat,row,column):
    print("Diagonal one: ", end="")
    for i in range(0,row):
        for j in range(0,column):
            # it this condition will become true then we will
            # get diagonal element.
            if (i==j):
                # printing square of diagonal element.
                print(mat[i][j]*mat[i][j])
    
    print("\n Diagonal two:")
    for i in range(0,row):
        for j in range(0,column):
            # if this condition will become true then we will get
            # second side diagonal element
            if (i+j==column-1):
                print(mat[i][j]*mat[i][j])

"""
Method 2:
An efiicient solution is also the same as in the naive approach but
in this, we are taking only one loop to find the diagonal element
and then we print the square of that element.
"""
def diagonalsquare(mat,row,column):
    print("Diagonal one: ")
    for i in range(0,row):
        print(mat[i][i]*mat[i][i])
    
    print("Diagonal 2:")
    for i in range(0,row):
        print(mat[i][row-i-1]*mat[i][row-i-1])
        

