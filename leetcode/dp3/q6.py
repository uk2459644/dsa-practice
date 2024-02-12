
class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
        


class Solution:
    def maxPathSum(self,root:list[TreeNode])->int:
        m=[1001]
        def solve(root,m):
            res=0
            if root:
                left=solve(root.left,m)
                right=solve(root.right,m)
                res=max(left+root.val,right+root.val,root.val)
                m[0]=max(m[0],left+right+root.val,res)
            
            return res
        solve(root,m)

        return m[0]
    
    