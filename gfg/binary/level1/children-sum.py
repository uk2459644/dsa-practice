"""
Program to check children sum property
Helper class that allocates a new node with the given data and None left and right pointers
"""

class newNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None

"""
Returns 1 if children sum property
holds for the given node and both 
of its children
"""
def isSumProperty(node):
    # left_data is left child data and
    # right_data is for right child data 
    left_data = 0
    right_data = 0
    # if node is None or it's a leaf 
    # node then return true
    if (node == None or (node.left == None and node.right == None)):
        return 1
    else:
        # If left child is not present then 
        # 0 is used as data of left child 
        if (node.left != None):
            left_data = node.left.data 
        # if right child is not present then 
        # 0 is used as data of right child 
        if (node.right != None):
            right_data = node.right.data
        # if the node and both of its children
        # satisfy the property return 1 else 0
        if((node.data == left_data + right_data) and isSumProperty(node.left) and isSumProperty(node.right)):
            return 1
        else:
            return 0
        