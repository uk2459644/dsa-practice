"""
Method 2:
This method doesn't use any auxiliary space to store values in the vector.
Create a 2D matrix of the given size. Now the idea is to traverse the tree
in PreOrder. while traversing, keep track of the last ancestor.

When we visit a node, if the node is NULL return, else assign M[lastancestor][currentNodeValue]=1

"""
size=6

M=[[0 for i in range(size)] for i in range(size)]

# a binary tree node
class Node:
    def __init__(self,data) -> None:
        self.left=self.right=None
        self.data=data

# helper function to create a new node
def newNode(data):
    temp=Node(data)
    return temp

def printMatrix():
    for i in range(size):
        for j in range(size):
            print(M[i][j],end=" ")

# First oreorder traversal
def MatrixUtil(root:Node,index):
    if root == None:
        return 
    
    preData=root.data
    # since there is no ancestor for root node, so we doesn't assign it's
    # value as 1 
    if (index==-1):
        index=root.data
    else:
        M[index][preData]=1
    
    MatrixUtil(root.left,preData)
    MatrixUtil(root.right,preData)

def Matrix(root):
    # call function MatrixUtil
    MatrixUtil(root,-1)

    # applying transitive closure
    # for the given matrix 
    for i in range(size):
        for j in range(size):
            for k in range(size):
                M[j][k]=(M[j][k] or (M[j][i] and M[i][k]))

        


