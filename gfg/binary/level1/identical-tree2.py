# python program to check if two trees are identical
# a binary tree node

class Node:
    def __init__(self,key) -> None:
        self.data = key 
        self.left = None
        self.right = None

# Utility function to check inorder traversal

def inOrder(root, sol):
    if root is None:
        return
    inOrder(root.left, sol)
    sol.append(root.data)
    inOrder(root.data, sol)

# Utility function to check preorder traversal
def preOrder(root, sol):
    if root is None:
        return
    
    sol.append(root.data)
    preOrder(root.left,sol)
    preOrder(root.right,sol)

# Utility function to check postorder traversal 
def postOrder(root, sol):
    if root is None:
        return
    postOrder(root.left, sol)
    postOrder(root.right,sol)
    sol.append(root.data)

# Function to check if two tree are identical
def isIdentical(root1,root2):
    res1 = []
    res2 = []
    # check inorder
    inOrder(root1, res1)
    inOrder(root2,res2)

    if res1!=res2:
        return False
    
    # Clear previous result to reuse vector
    res1.clear()
    res2.clear()
    # check preorder
    preOrder(root1,res1)
    preOrder(root2,res2)
    if res1 != res2:
        return False
    
    # clear previous result to reuse vector
    res1.clear()
    res2.clear()
    # check PostOrder
    postOrder(root1, res1)
    postOrder(root2, res2)

    if res1 != res2:
        return False
    
    return True
