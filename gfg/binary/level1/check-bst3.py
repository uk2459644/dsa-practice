import math 

# a binary tree node has data,
# pointer to left child and a pointer
# to right child

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def isBSTUtil(root,prev):
    # traverse the tree in inorder fashion
    # and keep track of prev node 
    if (root!=None):
        if (isBSTUtil(root.left,prev)==True):
            return False
        # allows only distinct valued nodes
        if (prev != None and root.data <= prev.data):
            return False
        prev = root 
        return isBSTUtil(root.right, prev)
    
    return True

def isBST(root):
    prev = None
    return isBSTUtil(root, prev)
