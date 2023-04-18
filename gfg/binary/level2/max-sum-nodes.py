# Python program to find maximum sun from a subset
# of nodes of binary tree 

# A binary tree node structure 
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None 

# Utility function to create
# a new Binary tree node 

def newNode(data):
    temp = Node(data)
    return temp 

# method returns maximum sum possible
# from subtrees rooted at grandChildren of node

def sumOfGrandChildren(node,mp):
    sum =0 
    # call for children of left
    # child only if it is not NULL
    if (node.left):
        sum+=(getMaxSumUtil(node.left.left,mp)+getMaxSumUtil(node.left.right,mp))
    
    # call for children of right 
    # child only if it is not Null
    if (node.right):
        sum+=(getMaxSumUtil(node.right.left,mp)+getMaxSumUtil(node.right.right,mp))
    
    return sum


# Utility method to return 
# maximum sum rooted at node 

def getMaxSumUtil(node, mp):
    if (node == None):
        return 0
    
    # If node is already processed 
    # then return calculated value from map
    if node in mp:
        return mp[node]
    
    # take current node value 
    # and call for all grand children 
    incl = (node.data+sumOfGrandChildren(node,mp))

    # don't take current node value
    # and call for all grand children 
    excl = (getMaxSumUtil(node.left,mp)+getMaxSumUtil(node.right,mp))

    # Choose maximum from both 
    # above call and store that in map 
    mp[node] = max(incl,excl)
    return mp[node]

# Returns maximum sum from 
# subset of nodes of binary 
# tree under given constraints 

def getMaxSum(node):
    if (node == None):
        return 0
    mp = dict()
    return getMaxSumUtil(node,mp)
