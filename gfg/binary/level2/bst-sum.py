# Program to transform a BST to sum tree

class Node:
    def __init__(self,x) -> None:
        self.data = x
        self.left = None
        self.right = None

# Recursive function to transform a BST to sum tree.
# This function traverse the tree in reverse inorder
# so, that we have visited all greater key nodes of the current
# visited node

def transformTreeUtil(root):
    # Base case 
    if (root == None):
        return
    # recur for right subtree 
    transformTreeUtil(root.right)
    # update sum 
    global sum
    sum=sum+root.data 
    # store old sum in current node 
    root.data = sum - root.data 
    # recur for left subtree 
    transformTreeUtil(root.left)

# A wrapper over transformTreeUtil()
def transformTree(root):
    transformTreeUtil(root)

# A utility function to printorder traversal of a
# binary tree 
def printInorder(root):
    if (root == None):
        return
    
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)
    