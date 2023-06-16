"""
Valid Sudoku  Configuration

Every number between 1 to9 appears only once in every row,column and
3x3 box of the sudoku. So check for every cell  of the configuration
that it's  value is appearing only once in it's row,column and 3x3 box.

"""
"""
Approach:

- Loop over every cell of the  sudoku 
- For every cell check,if that value appears only once in its row, column,
  and 3x3 box. If it is so then move on, else return false
- Repeat this process until all cells have been checked
- After this process return true, as no cell  was violating the conditions

"""
# checks whether there  is any duplicate in current row or not

def notInRow(arr,row):
    # set to  store  characters seen so far
    st=set()

    for i in range(0,9):
        # if already encountered before,return false
        if arr[row][i] in st:
            return False
        # If it is not an empty cell, insert value at the current cell
        # in the set
        if arr[row][i] != ".":
            st.add(arr[row][i])
    
    return True

# Checks whether there is any duplicate in current column or not
def notInCol(arr,col):
    st=set()

    for i in range(0,9):
        # if already encountered before,
        # return false
        if arr[i][col] in st:
            return False
        
        # If it is not an empty cell, insert value at the current cell
        # in the set
        if arr[i][col] != ".":
            st.add(arr[i][col])
    
    return True

# Checks whether there is any duplicate in current 3x3 box or not

def notInBox(arr,startRow,startCol):
    st=set()
    for row in range(0,3):
        for col in range(0,3):
            curr=arr[row+startRow][col+startCol]
            # if already encountered before, return false
            if curr in st:
                return False
            
            # if it is not an empty cell, insert value at current
            # cell in set
            if curr != ".":
                st.add(curr)
    
    return True

# Checks whether current row and current col and current box is valid
# or not

def isValid(arr,row,col):

    return (notInRow(arr,row) and notInCol(arr,col) and notInBox(arr,row-row%3,col-col%3) )

def isValidConfig(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            # if current row,col or box is not valid, return false
            if not isValid(arr,i,j):
                return False
    
    return True