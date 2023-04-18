"""
Program to find LCA of n1 and n2 using one traversal of
Binary tree 
It handles all cases even when n1 or n2 is not there in tree 
"""

class Node:
    # constructor to create a new node
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None 
        self.right = None 

"""
This function return pointer to LCA of two given values
n1 and n2
v1 is set as true by this function if n1 is found
v2 is set as true by this function if n2 is found
"""
def findLCAUtil(root,n1,n2,v):
    # Base case 
    if root is None:
        return None
    
    """
    If either n1 or n2 matches ith root's key, report
    the presence by setting v1 or v2 as true and return
    root (Note that if a key is ancestor of other, then
    the ancestor key becomes LCA)
    """
    if root.key == n1:
        v[0] = True
        return root
    
    if root.key == n2:
        v[1] = True 
        return root
    
    # Look for key in left and right subtree 
    left_lca = findLCAUtil(root.left, n1,n2,v)
    right_lca = findLCAUtil(root.right, n1,n2,v)

    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca is not None else right_lca

def find(root,k):
    # Base case 
    if root is None:
        return False
    
    if (root.key == k or find(root.left,k) or find(root.right,k)):
        return True 
    
    return False

def findLCA(root,n1,n2):
    # initialize n1 and n2 as not visited 
    v=[False, False]
    lca = findLCAUtil(root,n1,n2,v)

    if (v[0] and v[1] or v[0] and find(lca,n2) or v[1] and find(lca,n1)):
        return lca
    return None


