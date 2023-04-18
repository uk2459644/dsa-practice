# Program to print nodes of extreme corners
# of each level in alternate order 

# utility class to create a node 
class Node:
    def __init__(self,key) -> None:
        self.data = key 
        self.left = self.right = None 

# utility function to create a tree node 
def newNode(data):
    temp = Node(data)
    return temp

# Function to print nodes of extreme corners of
# each level in alternate order 
def printExtremeNodes(root):
    if (root == None):
        return 
    # creates a queue and enqueue left and right
    # children of rooot 
    q=[]
    q.append(root)
    # flag to indicate whether leftmost node or the
    # rightmost node has to be printed 
    flag = False 
    while (len(q)>0):
        # nodeCount indicates number of nodes 
        # at current level 
        nodeCount = len(q)
        n= nodeCount
        

