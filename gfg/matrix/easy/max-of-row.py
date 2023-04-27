"""
Given a matrix, the task is to find the maximum element of each row.

Approach: Approach is very simple. the idea is to run the loop for no_of_rows.
Check each element inside the row and find for the maximum element. Finally
print the element.
"""

def maxelement(arr):
    no_of_rows=len(arr)
    no_of_cols=len(arr[0])

    for i in range(no_of_rows):
        max1=0
        # initializing max1 to 0 at beginning
        # of finding max element of each row
        for j in range(no_of_cols):
            if arr[i][j]>max1:
                max1=arr[i][j]
        
        print(max1)

"""
Approach 2: Using nested loops
- Iterate through each row of the matrix.
- Initialize a variable to store the maximum element in the row.
"""
def max_element(matrix):
    result=[]
    for row in matrix:
        max_val=row[0]
        for val in row:
            if val>max_val:
                max_val=val
        
        result.append(max_val)
    return result

"""
Approach 3: Using List Comprehension

It is a concise way of creating a list in Python. We iterate through each 
row in the matrix using list comprehension and find the maximum element in the
current row using the max() function. We then append the maximum element to a new list.
"""
matrix=[[]]

output=[max(row) for row in matrix]
