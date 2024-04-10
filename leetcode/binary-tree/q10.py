
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def subTree(self,root:TreeNode):

        def dfs(level,node):
            if not node:
                return level,node
            
            ll,ln=dfs(level+1,node.left)
            rl,rn=dfs(level+1,node.right)

            if ll>rl:
                return ll,ln
            elif ll<rl:
                return rl,rn
            
            return ll,node
    





