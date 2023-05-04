"""
Given a matrix of n*n size, the task is to find whether all rows are
circular rotations of each other or not.

Algorithm:
1. Create a string of first row elements and concatenate the string with 
   itself so that string search operations can be efficiently performed
   LEt this string be str_cat.

2. Traverse all remaining rows. For every row being traversed, create a 
   string str_count of current row elements, if str_curr is not a substring
   of str_cat, return false.
"""

MAX=1000

def isPermutedMatrix(mat,n):
    # creating a string that contains elements of first row.
    str_cat=""
    for i in range(n):
        str_cat=str_cat+"-"+str(mat[0][i])
    # concatenating the string with itself so that substring search operation
    # can be performed on this.
    str_cat=str+str_cat
    # start traversing remaining rows
    for i in range(1,n):
        # store the matrix in vector in the form of string
        curr_str=""
        for j in range(n):
            curr_str=curr_str+"-"+str(mat[i][j])
        
        # Check if the current string is present in the 
        # concatenated string or not
        if (str_cat.find(curr_str)):
            return True
    
    return False



