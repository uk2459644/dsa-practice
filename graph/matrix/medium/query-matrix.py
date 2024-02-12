"""
Given a matrix M of size mxn. it is initially filled with integers from 1 to
mxn sequentially in a row major order. The task is to process a list of queries
manipulating M such that every query is one of the following three.

1.R(x,y): swaps the x-th and y-th rows of M where x and y vary from 1 to m.
2. C(x,y): swaps the x-th and y-th columns of M where x and y vary from 1 to n.
3. P(x,y): prints the element at x-th row and y-th column where x varies from 1 to m
   and y varies from 1 to n.

An efficient approach for this problem requires little bit mathematical observation.
Here we are given that elements in matrix are filled from 1 to mxn sequentially
in row major order, so we will take advantage of this given scenario and can solve this 
problem.

- Create an auxiliary array rows[m] and fill it with values 0 to m-1 sequentially.

- Create another auxiliary array cols[n] and fill it values 0 to n-1 sequentially.

- Now for query R(x,y) just swap the value of rows[x-1] with rows[y-1].

- Now for query C(x,y) just swap the value of cols[x-1] with cols[y-1].

- Now for query P(x,y) just skip the number of columns you have seen and
  calculate the value at (x,y) by rows[x-1]*n+cols[y-1]+1
"""
def preprocessMatrix(rows,cols,m,n):
    for i in range(m):
        rows[i]=i
    
    for i in range(n):
        cols[i]=i

def queryMatrix(rows,cols,m,n,ch,x,y):
    tmp=0
    if ch=='R':
        rows[x-1],rows[y-1]=rows[y-1],rows[x-1]
    elif ch=='C':
        cols[x-1],cols[y-1]=cols[y-1],cols[x-1]
    elif ch=='P':
        print(rows[x-1]*n+cols[y-1]+1)
        
