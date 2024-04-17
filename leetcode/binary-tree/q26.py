class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sumNumber(self,root:TreeNode):
        if not root:
            return 0
        
        def dfs(node,sm):
            if node:
                sm=sm*10+node.val
                if not node.left and not node.right:
                    return sm
                left=dfs(node.left,sm)
                right=dfs(node.right,sm)

                return left + right
            
            return 0
        
        return dfs(root,0)
