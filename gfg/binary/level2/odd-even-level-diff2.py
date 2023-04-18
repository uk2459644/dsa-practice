# A recursive program to find difference between sum of 
# nodes at odd level and sum at even level 

# A binary tree node 
class Node:
    # constructor to create a new node 
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# The main function that returns differnece between odd and 
# even level nodes 

def getLevelDiff(root):
    # Base case 
    if root is None:
        return 0
    
    # Difference for root is root's data - difference for
    # left subtree - difference for right subtree 
    return (root.data - getLevelDiff(root.left) - getLevelDiff(root.right))


