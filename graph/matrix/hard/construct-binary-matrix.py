"""
Construct Ancestor Matrix from a Given Binary Tree

Method 1: 
The idea is to traverse the tree. While traversing, keep track of ancestor
in array. When we visit a node, we add it to ancestor array and consider
the corresponding row in the adjacency matrix. We mark all ancestors in its
row as 1. Once a node and all its children are processed, we remove the node
from ancestor array.

"""
class newnode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

# anc[] stores all ancestors of current node. This function fills ancestors
# for all nodes. It also returns size of tree. Size of tree is used to print
# ancestor matrix.

def ancestorMatrixRec(root,anc):
    global mat,MAX 
    # base case
    if root == None:
        return 0
    # update all ancestor of current node
    data=root.data
    for i in range(len(anc)):
        mat[anc[i]][data]=1
    
    # push data to list of current node
    anc.append(data)
    # traverse left and right subtree
    l=ancestorMatrixRec(root.left,anc)
    r=ancestorMatrixRec(root.right,anc)
    # remove data from list the list of ancestors as all descendants of it
    # are processed now.
    anc.pop(-1)

    return l+r+1

def ancestorMatrix(root):
    # create an empty ancestor array
    anc=[]
    # fill ancestor matrix and find size of tree
    n=ancestorMatrixRec(root,anc)
    # prin the filled values
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
            
