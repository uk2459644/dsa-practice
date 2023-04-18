
class Node:
    def __init__(self,key) -> None:
        self.key = key 
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    
    # Create a stack to store the left and right subtree of root

    stack = []
    stack.append(root.left)
    stack.append(root.right)

    # continue to loop until the stack is empty
    while stack:
        # Pop the left and right subtree from the stack
        node1 = stack.pop()
        node2 = stack.pop()

        # if both nodes are null, continue the loop
        if not node1 and not node2:
            continue

        # if one of the  nodes is null, the binary tree is not symmetric
        if not node1 or not node2:
            return False
        
        # if the values of the nodes are not equal, the
        if node2.key != node1.key:
            return False
        
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
    
    return True
