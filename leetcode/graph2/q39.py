
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]
n=len(root)
def buildTree(i):
    if i<n:
        node=TreeNode(root[i])
        node.left=buildTree(2*i+1)
        node.right=buildTree(2*i+2)

        return node
    return None

tree=buildTree(0)
limit=1

def dfs(node,sm):
    if not node:
        return False
    
    sm+=node.val
    if not node.left and not node.right:
        return sm>=limit
    
    left=dfs(node.left,sm)
    right=dfs(node.right,sm)

    if not left:
        node.left=None
    if not right:
        node.right=None
    
    return left or right





