# Python program to find largest value
# on each level of binary tree 

def helper(res,root,d):
    if (not root):
        return 
    # expand list size 
    if (d==len(res)):
        res.append(root.val)
    else:
        res[d]=max(res[d],root.val)
    
    helper(res,root.left,d+1)
    helper(res,root.right,d+1)

def largestValues(root):
    res=[]
    helper(res,root,0)
    return res

class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None
        
