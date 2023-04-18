"""
Python program to check if a binnary tree is bst or not
a binary tree node has data, pointer to let child and a
pointer to right child
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None

def maxValue(node):
    if node is None:
        return 0
    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)

    value =0
    if leftMax > rightMax:
        value = leftMax
    else:
        value = rightMax
    
    if value < node.data :
        value = node.data 
    
    return value

def minValue(node):
    if node is None:
        return 1000000000
    
    leftMax = minValue(node.left)
    rightMAx = minValue(node.right)

    value = 0
    if leftMax < rightMAx :
        value = leftMax
    else :
        value = rightMAx
    
    if value > node.data:
        value = node.data 
    
    return value 

def isBST(node):
    if node is None:
        return True
    
    # false if the max of the left is > node 
    if (node.left is not None and maxValue(node.left)>node.data):
        return False
      
    # false if the min of the right is <= than us
    if(node.right is not None and minValue(node.right) < node.data):
        return False
     
    #false if, recursively, the left or right is not a BST
    if(isBST(node.left) is False or isBST(node.right) is False):
        return False
     
    # passing all that, it's a BST
    return True
 
