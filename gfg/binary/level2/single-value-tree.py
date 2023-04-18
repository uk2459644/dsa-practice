
# Python program to find the count of single
# valued subtrees 

# Node Structure 
class Node:
    # utility function to create a new node 
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

"""
This function increments count by number of single
valued subtrees under root. It Returns true if subtree
under root is Singly, else false.
"""
def countSingleRec(root, count):
    if root is None:
        return True
    left = countSingleRec(root.left, count)
    right = countSingleRec(root.right, count)

    # If any of the subtrees is not singly, then this
    # cannot be singly 
    if left == False or right ==False:
        return False
    # If left subtree is singly and non-empty,
    # but data doesn't match
    if root.left and root.data != root.left.data:
        return False 
    # same for right subtree 
    if root.right and root.data != root.right.data:
        return False 
    
    # If none of the above conditions is True, then
    # tree rooted under root is single valued, increment
    # count and return true 
    count[0]+=1 
    return True 

def countSingle(root):
    count = [0]
    # Recursive function to count 
    countSingleRec(root,count)
    return count[0]
