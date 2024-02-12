"""
Method 4: Using Map

1. Insert all the elments of the 1st row in the map
2. Now we check that the elements present in the map are present in each row
   or not.
3. If the element is present in the mao and is not duplicated in the current
   row, then we increment the count of the element in the map by 1.
4. If we reach the last row while traversing and if the element appears (N-1)
   times before then we print the element.

"""

def distinct(matrix,N):
    ans={}
    # insert the elements of first row in the map and
    # initialize with 1
    for j in range(N):
        ans[(matrix[0][j])]=0
    
    # traverse the matrix from 2nd row
    for i in range(N):
        for j in range(N):
            # if the element is present in the map
            # and is not duplicated in the current row
            if matrix[i][j] in ans and ans[(matrix[i][j])]==i:
                # increment count of the element in map by 1
                ans[(matrix[i][j])]=i+1
                # if we have reached the last row
                if (i==N-1):
                    print(matrix[i][j])
                    