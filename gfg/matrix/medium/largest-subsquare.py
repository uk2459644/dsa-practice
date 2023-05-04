"""
Given a matrix of 'O' and 'X', find the largest subsquare surrounded by
'X'

A Simple Solution is to consider every square submatrix and check whether
is has all corner edges filled with 'X'. The time complexity of this solution
is O(N4).

We can solve this problem in O(N3) time using extra space. The idea is to
create two auxiliary arrays hor[N][N] and ver[N][N]. the value stored in
how[i][j] is the number of horizontal continuous 'X' character till mat[i][j]
in mat[][]. Similarly, the value stored in ver[i][j] is the number of vertical
continuous 'X' characters till mat[i][j] in mat[][].

"""

import math as mt

N=6

def getMin(x,y):
    if x<y:
        return x
    else:
        return y

def findSubSquare(mat):
    Max=0
    # initialize the left-top value in hor[][] and ver[][]
    hor=[[0 for i in range(N)] for i in range(N)]
    ver=[[0 for i in range(N)] for i in range(N)]

    if mat[0][0]=='X':
        