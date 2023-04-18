# Binary tree node structure
class Node:
    def __init__(self,x) -> None:
        self.data = x
        self.right = None 
        self.left = None 

# an iterative function to do postorder
# traversal of a given binary tree 

def postOrderIterative(root):
    stack = []
    check = True 

    while True:
        while (root != None):
            stack.append(root)
            root = root.left 
        
        # if the stack is empty, the traversal is finished
        if (len(stack)==0):
            return 
        # To avoid infinite looping this check is necessary
        if (root != stack[-1].right):
            root = stack[-1].right 
            check = True 
            continue 
        root = stack.pop()
        print(root.data, end=" ")
        check= False 
    