# Program for boundary traversal of binary tree


# a binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# A simple funtion to print leaf nodes of a binary tree 

def printLeaves(root):
    if (root):
        printLeaves(root.left)
        # print if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data)
        printLeaves(root.right)

# A function to print all left boundary nodes, except
# a leaf node. Print the nodes in Top Down manner

def printBoundaryLeft(root):
    if root:
        if (root.left):
            # to ensure top down order, priint the node
            # before calling itself for left subtree
            print(root.data)
            printBoundaryLeft(root.left)
        elif (root.right):
            print(root.data)
            printBoundaryLeft(root.right)
        
        # do nothing if it is a leaf node, this way we
        # avoid duplicate inn output 

# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in Bottom up manner

def printBoundaryRight(root):
    if (root):
        printBoundaryRight(root.right)
        print(root.data)
    elif (root.left):
        printBoundaryRight(root.left)
        print(root.data)
    # do nothing if it is a leaf node, this way
    # we avoid duplicates in output 

def printBoundary(root):
    if (root):
        print(root.data)
        # print the left boundary in top-down manner
        printBoundaryLeft(root.left)
        # print all leaf nodes 
        printLeaves(root.left)
        printLeaves(root.right)
        # print the right boundary in bottom-up manner
        printBoundaryRight(root.right)
        