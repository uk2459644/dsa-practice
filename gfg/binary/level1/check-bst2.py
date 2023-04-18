
INT_MAX = 429467296
INT_MIN = -429467296

class Node:
    # constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None 

# Return true if the given tree is a binary search tree
def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
    
    return (isBSTUtil(node.left, mini, node.data -1) and isBSTUtil(node.right, node.data+1,maxi))
