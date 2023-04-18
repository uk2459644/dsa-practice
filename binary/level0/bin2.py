# python program to find the maximum depth of tree
# a binary tree node

class Node:
    # constructor to create a new node
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None
        self.right=None

# compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node

def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth=maxDepth(node.left)
        rDepth=maxDepth(node.right)
        # use the larger one
        if (lDepth>rDepth):
            return lDepth+1
        else:
            return rDepth+1


