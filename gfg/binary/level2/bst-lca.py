# Program to find LCA of n1 and n2 using one 
# traversal of Binary tree 

# A binary tree node 
class Node:
    # Constructor to create a new tree node 
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None 
        self.right = None 

# This function returns pointer to LCA of two given
# vlues n1 and n2 
# This function assumes that n1 and n2 are present in
# Binary Tree 

def findLCA(root,n1,n2):
    # BAse case 
    if root is None:
        return None 
    
    # if either n1 or n2 matches with root's key, report
    # the presence by returning root (Note that if a key is ancestor of other, then the
    # ancestor key become LCA)
    if root.key == n1 or root.key ==n2:
        return root
    # look for keys in left and right subtree 
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1,n2)

    # If both of the above calls return Non-NULL, then one key is 
    # present in once subtree and other is present in others 
    # So this node is the LCA 
    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca is not None else right_lca

