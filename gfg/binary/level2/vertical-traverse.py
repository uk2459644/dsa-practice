# program for printing vertical order of a given
# binary tree 

# a binary tree node 
class Node:
    # constructor to create a new node
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None 
        self.right = None 

# Utility function to store vertical order in map 'm
# 'hd' is horizontal distance of current node from root
# 'hd' is initially passed as 0

def getVerticalOrder(root, hd, m):
    # Base case 
    if root is None:
        return
    # Store current node in map 'm'
    try:
        m[hd].append(root.key)
    except:
        m[hd]=[root.key]
    
    # stores nodes in left subtree 
    getVerticalOrder(root.left, hd-1,m)
    # stores nodes in right subtree 
    getVerticalOrder(root.right,hd+1,m)

# The main function to print vertical order of a
# binary tree ith given root 

def printVerticlOrder(root):
    m=dict()
    hd=0
    getVerticalOrder(root,hd,m)

    # Traverse the map and print nodes at every horizontal
    # distance {hd}
    for index,value in enumerate(sorted(m)):
        for i in m[value]:
            print(i,end=" ")

        print()

