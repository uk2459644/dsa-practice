
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def tree2str(self,root:TreeNode):
        def dfs(node):
            if not node:
                return ""
            
            s=str(node.val)
            if node.right and not node.left:
                s+="()"+"("+dfs(node.right)+")"
            elif node.left and not node.right:
                s+="("+dfs(node.left)+")"
            elif node.left and node.right:
                s+="("+dfs(node.left)+")"+"("+dfs(node.right)+")"
            
            return s
        
        return dfs(root)





