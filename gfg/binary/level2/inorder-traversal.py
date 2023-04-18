
# Program to do inorder traversal without 
# recursion 

# a binary tree node 
class Node:
    # constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# Iterative function for inorder tree traversal 

def inOrder(root):
    # set current to root of binary tree
    current = root 
    stack = [] 

    while True:
        # Reach the left most Node of the current Node
        if current is not None:
            # Place pointer to a tree node on the 
            # stack before traversing the node's left subtree

            stack.append(current)
            current=current.left 
        # Backtrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done 
        elif (stack):
            current = stack.pop()
            print(current.data, end=" ")
            # we have visited the node and its left subtree
            # now, it's right subtree's turn
            current = current.right 
        else:
            break 
    print()
    
