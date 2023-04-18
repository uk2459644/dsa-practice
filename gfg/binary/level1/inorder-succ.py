# Program to find the inorder successir in a BST 
# A binary tree node

class Node:
    # Constructor to create a new node
    def __init__(self,key) -> None:
        self.data = key
        self.left = None
        self.right = None

def inOrderSuccessor(n):
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)

    p=n.parent
    while (p is not None):
        if n!= p.right:
            break
        n=p
        p=p.parent 
    return p


# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched

def minValue(node):
    current = node
    # loop down to find the leftmost leaf
    while (current is not None):
        if current.left is None:
            break
        current = current.left
    return current

"""
Given a binary search tree and a number, insert a new
node with the given number in the correct place
in the tree. Returns the new root pointer which the 
caller should then use (the standard trick to avoid 
using reference parameters)
"""

def insert(node, data):
    # If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp 
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        # return the unchanged pointer
        return node
    