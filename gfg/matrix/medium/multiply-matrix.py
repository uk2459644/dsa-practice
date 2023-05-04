"""
Multiply two matrices.
"""

def mulMat(mat1,mat2,R1,R2,C1,C2):
        #    list to store matrix multiplication result
        rslt=[[0]*C2 for i in range(R1)]

        for i in range(0,R1):
                for j in range(0,C2):
                        for k in range(0,R2):
                                rslt[i][j]+=mat1[i][k]*mat2[k][j]

"""
Program to multiply two rectangular matrices.
"""                     
def multiply(m1,m2,mat1,n1,n2,mat2):
        res=[[0 for x in range(n2)] for y in range(m1)]

        for i in range(m1):
                for j in range(n2):
                        res[i][j]=0
                        for x in range(m2):
                                res[i][j]+=mat1[i][x]*mat2[x][j]
        
        
