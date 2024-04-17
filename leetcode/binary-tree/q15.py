
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def addRow(self,root:TreeNode,val:int,depth:int):
        if not root:
            return 
        
        if depth==1:
            nd=TreeNode(val)
            nd.left=root
            return nd
        
        def dfs(node:TreeNode,lv:int):
            if node:
                if lv==depth-1:
                    tm_left=node.left
                    tm_right=node.right
                    nd1=TreeNode(val)
                    nd2=TreeNode(val)
                    node.left=nd1
                    node.right=nd2
                    node.left.left=tm_left
                    node.right.right=tm_right
                
                node.left=dfs(node.left,lv+1)
                node.right=dfs(node.right,lv+1)

                return node
            
            return None
        
        return dfs(root,1)




