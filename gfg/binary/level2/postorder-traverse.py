# Python program for iterative postorder traversal 
# using one stack 

# stores the answer
ans = []

# a binary tree node 
class Node:
    # constructor to create a new node 
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    return None 

# A iterative function to do postorder traversal of 
# a given binary tree 

def postOrderIterative(root):
    if root is None:
        return 
    stack = []
    while True:
        while root:
            # push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            # set root as root's left child 
            root = root.left 
        # pop an item from stack and set it as root
        root = stack.pop()
        # If the popped item has a right child and the right child
        # is not processed yet, then make sure right child is processed
        # before root
        if (root.right is not None and peek(stack) == root.right):
            stack.pop()
            stack.append(root)
            root = root.right 
        else:
            ans.append(root.data)
            root = None 
        
        if len(stack)<=0:
            break