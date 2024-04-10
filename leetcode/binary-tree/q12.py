
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:

    def trimBST(self,root:TreeNode,low:int,high:int):

        def dfs(node:TreeNode):
            if node:

                if node.val<low:
                    return dfs(node.right)

                if node.val > high:
                    return dfs(node.left)
                
                node.left=dfs(node.left)
                node.right=dfs(node.right)

                return node
            
            return None
        
        return dfs(root)
    
    
            






