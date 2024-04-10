
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxRowVal(self,root:TreeNode):
        if not root:
            return []
        
        ans=[]

        def dfs(level,node:TreeNode):
            if not node:
                return
            
            if len(ans)==level:
                ans.append(node.val)
            
            ans[level]=max(ans[level],node.val)
            dfs(level+1,node.left)
            dfs(level+1,node.right)
        
        dfs(0,root)

        return ans


