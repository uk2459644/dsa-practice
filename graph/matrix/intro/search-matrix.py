"""
Given a matrix mat[][] of size NXM, where every row and column is sorted
in increasing order, and a number X is given. The task is to find whether
element X is present in the matrix or not.

Solution: 
A Simple solution is to one by one compare x with every element of the 
matrix. If matches, then return true. If we reach the end then return false.
The time complexity of this solution is O(nXm).
"""

def searchInMatrix(arr,x):
    for i in range(0,4):
        for j in range(0,5):
            if (arr[i][j]==x):
                return 1 
    
    return

"""
Time Complexity: O(MXN), where M and N are the numbers of rows
and columns respectively.
Auxiliary Space: O(1)
"""


