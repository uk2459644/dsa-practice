# Python implementation to convert a given
# BST to Max Heap 

i=0
class Node:
    def __init__(self) -> None:
        self.data = 0
        self.left = None
        self.right = None

# Helper function that allocates a new node with
# the given data and None left and right
# pointers.

def getNode(data):
    newNode = Node()
    newNode.data = data
    newNode.left = newNode.right = None
    return newNode

arr =[]
# function for the inorder traversal of the tree
# so as to store the node values in arr in 
# sorted order 

def inorderTraversal(root):
    if (root == None):
        return arr 
    # first recur on left subtree 
    inorderTraversal(root.left)
    # then copy the data of the node 
    arr.append(root.data)
    # now recur for right subtree 
    inorderTraversal(root.right)

def BSTToMaxHeap(root):
    global i
    if (root == None):
        return None
    # recur on left subtree 
    root.left = BSTToMaxHeap(root.left)
    # recur on right subtree 
    root.right = BSTToMaxHeap(root.right)
    # copy data at index 'i' or arr to the node
    root.data = arr[i]
    return root

# Utility function to convert the given BST to
# MAX HEAP 

def convertToMAxHeapUtil(root):
    global i 
    # vector to store the data of all the
    # nodes of the BST 
    i=0
    # inorder traversal to populate 'arr'
    inorderTraversal(root)
    # BST to MAX HEAP conversion 
    root = BSTToMaxHeap(root)
    return root

# Function to print postorder traversal of the tree
def postorderTraversal(root):
    if (root == None):
        return 
    
    # recur on left subtree 
    postorderTraversal(root.left)
    # then recur on right subtree 
    postorderTraversal(root.right)
    # print the root's data 
    print(root.data, end=" ")
    