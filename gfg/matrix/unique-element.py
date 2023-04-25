"""
Given a matrix mat[][] having n rows and m columns. We need to find
unique elements in the matrix, those elements not repeated in the matrix
or those whose frequency is 1.

Solution: 
The idea is to use hashing and traverse through all the elements of the 
matrix, If an element is present in the dictionary, then increment its count.
Otherwise insert an element with value=1.
"""
def unique(mat,n,m):
    maximum=0
    flag=0
    for i in range(n):
        for j in range(m):
            if maximum < mat[i][j]:
                maximum=mat[i][j]
    
    b=[0]*(maximum+1)
    for i in range(n):
        for j in range(m):
            y=mat[i][j]
            b[y]+=1 
    
    for i in range(1,maximum+1):
        if b[i]==1:
            print(i,end=" ")
    flag=1 
    if flag==0:
        print("No unique element in the matrix.")
        
