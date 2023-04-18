# python program to check if a given binary tree
# is symmetric or not
# node structure

class Node:
    def __init__(self,key) -> None:
        self.key=key 
        self.left=None
        self.right=None

# returns true is trees with root1 and root2
#  are mirror
def isMirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    
    if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return (isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left))
    
    return False

def isSymmetric(root):
    return isMirror(root,root)