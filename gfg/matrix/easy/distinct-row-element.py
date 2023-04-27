"""
Given a nxn matrix. The problem is to find all the
distinct elements common to all rows of the matrix.

Method 1:
Using three nested loops. Check if an element of 1st row is present in all
the subsequent rows.

Method 2:
Sort all the rows of the matrix individually in increasinng order.

"""
MAX=100

def sortRows(mat,n):
    for i in range(0,n):
        mat[i].sort()

def findAndPrintCommonElement(mat,n):
    sortRows(mat,n)
    curr_index=[0]*n

    for i in range(0,n):
        curr_index[i]=0
    
    f=0
    while(curr_index[0]<n):
        # value present at the current
        # column index of 1st row
        value=mat[0][curr_index[0]]
        present=True

        # value is being searched in all the subsequent rows
        for i in range(1,n):
            # iterate throough all the elements of the row from its
            # current column index till an element greater than the 
            # value is found or the end of the row is encountered.
            while (curr_index[i]<n and mat[i][curr_index[i]]<=value):
                curr_index[i]=curr_index[i]+1
            
            if (mat[i][curr_index[i]-1]!=value):
                present=False
            
            if (curr_index[i]==n):
                f=1
                break
            if present:
                print(value)
            
            if f==1:
                break

            curr_index[0]=curr_index[0]+1
            


