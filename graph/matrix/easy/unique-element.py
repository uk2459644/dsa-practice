"""
Given a matrix mat[][] having n rows and m columns. We need to find
unique elements in matrix, those elements which are not repeated in the 
matrix or those elements whose frequency is 1.

Follow these steps to find a unique element:

1. Create an empty hash table or dictionary.
2. Traverse through all the elements of the matrix.
3. If element is present in the dictionary, then increment its count.
4. Otherwise insert element with value=1.

"""
def unique(mat,n,m):
    maximum=0
    flag=0
    for i in range(0,n):
        for j in range(0,m):
            # find maximum element in a matrix
            if maximum<mat[i][j]:
                maximum=mat[i][j]
    
    uniqueElementDict=[0]*(maximum+1)
    # loops to traverse through the matrix
    for i in range(0,n):
        for j in range(0,m):
            uniqueElementDict[(mat[i][j])]+=1
    
    # print all those keys whose count is 1
    for key in range(maximum+1):
        if uniqueElementDict[key]==1:
            print(key)
            flag=1
    
    if flag==0:
        print("No unique element in the matrix")
        
