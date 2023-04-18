# program to check if a tree is height - balanced
# a binary tree node

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = self.right = None

# function to find height of binary tree
def height(root):
    if root is None:
        return 0
    
    return max(height(root.left),height(root.right))+1 

def isBalanced(root):
    if root is None:
        return True
    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh-rh) are 1,-1,0
    if (abs(lh-rh)<=1 and isBalanced(root.left) is True and isBalanced(root.right) is True):
        return True
    return False

