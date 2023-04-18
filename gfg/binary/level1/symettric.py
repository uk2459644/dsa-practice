# program to check if a given binary tree
# is symmetric or not

# node structure

class Node:
    # utility function to create new node
    def __init__(self,key) -> None:
        self.key = key 
        self.left = None
        self.right = None

# Returns true if trees
# with roots as root1 and root2 are mirror

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    """For two trees to be mirror images,
    the following three conditions must be true
    1 -  Their node's key must be same
    2 - Left subtree of the left tree and right subtree of right
      tree have to be mirror images 
    3 - right subtree of left tree and left subtree of right tree have
       to be mirror images"""
    
    if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return (isMirror(root1.left,root2.right) and isMirror(root1.right, root2.left))
    
    return False

def isSymmetric(root):
    return isMirror(root, root)

