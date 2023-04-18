# Program to check binary tree is a subtree of another tree

# a binary tree node
class Node:
    # constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# A utility function to check whether trees
# with roots as root 1 and root2 are identical or not

def areIdentical(root1, root2):

    # Base Case 
    if root1 is None and root2 is None:
        return True 
    if root1 is None or root2 is None:
        return False 
    
    # Check if the data of both roots is same 
    # and data of left and right subtree are also same
    return (root1.data == root2.data and areIdentical(root1.left,root2.left) and areIdentical(root1.right, root2.right))

# This function returns True if S is a subtree
# of T, otherwise False 

def isSubTree(T,S):
    if S is None:
        return True
    if T is None:
        return False
    # check the tree with root as current node
    if (areIdentical(T,S)):
        return True
    
    # If the tree with root as current node doesn't match
    # then try left and right subtree one by one
    return isSubTree(T.left, S) or isSubTree(T.right, S)
