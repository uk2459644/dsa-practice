# program to implement the level order 
# traversal approach

from queue import Queue

class Node:
    def __init__(self, val) -> None:
        self.data = val 
        self.left = None
        self.right = None

# Function to check if two trees are identical or not

def isIdentical(root1, root2):
    # Base case if both roots are None, then trees are
    # identical
    if not root1 and not root2:
        return True
    # If one of the roots is None, then trees are not
    # identical
    if not root1 or not root2:
        return False
    # Crete queues to preform level order traversal
    # on both trees
    q1 = Queue()
    q2 = Queue()
    # Add the roots of both trees to their 
    # respective queues
    q1.put(root1)
    q2.put(root2)

    # loop until either of the queues becomes empty
    while not q1.empty() and not q2.empty():
        curr1 = q1.get()
        curr2 = q2.get()

        # IF the data of the current nodes is not equal,
        # then trees are not identical 
        if curr1.data != curr2.data:
            return False
        
        # if the left child of none tree exists and the
        # left child of the other tree does not exist, then
        # trees are not identical
        if (curr1.left and not curr2.left) or (not curr1.left and curr2.left):
            return False
        
        if(curr1.right and not curr2.right) or (not curr1.right and curr2.right):
            return False
        
        if curr1.left and curr2.left:
            q1.put(curr1.left)
            q2.put(curr2.left)
        
        if curr1.right and curr2.right:
            q1.put(curr1.right)
            q2.put(curr2.right)
        
        return True
    
