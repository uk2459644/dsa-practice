
class node:
    def __init__(self,x) -> None:
        self.data = x 
        self.left = None 
        self.right = None 

def isLeaf(node):
    if(node==None):
        return 0
    if(node.left == None and node.right == None):
        return 1 
    return 0

def isSumTree(node):
    if (node==None):
        return 0
    
    ls=isSumTree(node.left)
    if (ls==-1):
        return -1 
    
    rs=isSumTree(node.right)
    if(rs==-1):
        return -1 
    
    if(isLeaf(node) or ls+rs == node.data):
        return ls+rs+node.data 
    else:
        return -1 
    
