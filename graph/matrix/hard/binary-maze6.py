"""
Given a matrix mat[][] containing the characters Z,P and * where Z is 
a zombie, P is a plant and * is a bare land. Given that a zombie can attack
a plant if the plant is adjacent to the zombie. The task is to print the number
of plants that are safe from the zombies.

"""

"""
Approach: Traverse the matrix element by element, if the current element
is a plant, mat[i][j]='P' then check if the plant is surrounded by any
zombie (in all the 8 adjacent cells). If the plant is safem then update
count=count+1. Print the count in the end.

"""
# Function that returns true if mat[i][j] is a zombie

def isZombie(i,j,r,c,mat):
    if (i<0 or j<0 or i>=r or j>=c or mat[i][j]!='Z'):
        return True
    
    return False

# function to return the count of plants that survived from the zombie
# attack

def plant_vs_zombie(mat,row,col):
    count=0
    for i in range(row):
        for j in range(col):
            if mat[i][j]=='P':
                # if current plant is safe from zombie
                if (isZombie(i-1,j-1,row,col,mat) and 
                    isZombie(i-1,j,row,col,mat) and 
                    isZombie(i-1,j+1,row,col,mat) and
                    isZombie(i,j-1,row,col,mat) and 
                    isZombie(i,j,row,col,mat) and 
                    isZombie(i,j+1,row,col,mat) and 
                    isZombie(i+1,j-1,row,col,mat) and 
                    isZombie(i+1,j,row,col,mat) and 
                    isZombie(i+1,j+1,row,col,mat)):
                    count+=1

    return count


