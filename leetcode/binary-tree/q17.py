
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def bottomLeftLeave(self,root:TreeNode):
        lvl=-1
        ans=0

        def dfs(node,lv):
            nonlocal lvl,ans

            if node:
                if lv>lvl:
                    lvl=lv
                    ans=node.val
                dfs(node.left,lv+1)
                dfs(node.right,lv+1)
        
        dfs(root,0)

        return ans
                





