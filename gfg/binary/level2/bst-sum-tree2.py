# Python program to check if Binary tree is sum
# tree or not

# A binnary tree node has data,
# left child and right child
class Node:
    def __init__(self,x) -> None:
        self.data =x
        self.left = None
        self.right = None 

def isLeaf(node):
    if (node==None):
        return 0
    if (node.left == None and node.right == None):
        return 1
    return 0

# A utility function to get the sum of
# values in tree with root as root

def sum(root):
    if (root==None):
        return 0
    
    return (sum(root.left)+root.data+sum(root.right))

# returns 1 if SumTree property holds
# for the given tree
def isSumtree(node):
    # If node is None or 
    # it's a leaf node then return true
    if(node == None or isLeaf(node)):
        return 1
    
    if(isSumtree(node.left) and isSumtree(node.right)):
        # Get the sum of nodes in left subtree 
        if (node.left == None):
            ls=0
        elif(isLeaf(node.left)):
            ls=node.left.data 
        else:
            ls=2*(node.left.data)
        # Get the sum of nodes in right subtree 
        if(node.right == None):
            rs=0
        elif(isLeaf(node.right)):
            rs=node.right.data
        else:
            rs=2*(node.right.data)
        
        # If root's data is equal to sum of nodes
        # in left and right subtrees then return 1 
        # else return 0
        return (node.data==ls+rs)
    
    return 0

