# Program to perform iterative preorder traversal

# a binary tree node 
class Node:
    # Contstructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# An iterative process to print preorder traversal of BST 

def iterativePreorder(root):
    # base case 
    if root is None:
        return 
    
    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)
    """
    Pop all items one by one. Do following for every
    popped item
    1 print it
    push its right child 
    push its left child 
    right child is pushed first so that left
    is processed first
    """
    while (len(nodeStack)>0):
        node = nodeStack.pop()
        print(node.data, end=" ")
        # push right and left children of the
        # popped node to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
            

