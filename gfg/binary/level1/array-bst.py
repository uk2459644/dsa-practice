# Python program to convert sorted array to bst

# binary tree node

class Node:
    def __init__(self,d) -> None:
        self.data = d
        self.left = None 
        self.right = None

# function to convert sorted array to a
# balanced tree
# input : sorted array of integers 
# output : root node of balanced BST 

def sortedArrayToBST(arr):
    if not arr:
        return None 
    mid = (len(arr))//2 
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])

    return root

# A utility function to print the preorder traversal of the BST

def preOrder(node):
    if not node:
        return 
    
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)
    