# Python program to implement
# the above approach
# A binary tree node has data,
# left child and right child

class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.left = None 
        self.right = None

# A utility function to get the sum
# of values in tree with root as root

def sum(root):
    if (root==None):
        return 0
    return (sum(root.left)+root.data+sum(root.right))

# Returns 1 if sum property holds
# for the given node and both of
# its children

def isSumTree(node):
    if (node == None or (node.left == None and node.right==None)):
        return 1
    # Get sum of nodes in left and
    # right subtree
    ls=sum(node.left)
    rs=sum(node.right)
    # If the node and both of its children
    # satisfy the property return 1 else 0
    if((node.data==ls+rs) and isSumTree(node.left) and isSumTree(node.right)):
        return 1 
    return 0
