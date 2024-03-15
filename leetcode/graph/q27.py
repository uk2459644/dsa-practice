
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxProduct(self,root:TreeNode):
        sm_dic=list()

        def dfs(node:TreeNode):
            res=node.val

            if node.left:
                res+=dfs(node.left)
            if node.right:
                res+=dfs(node.right)
            
            sm_dic.append(res)
            return res
        
        dfs(root)
        sorted_values = sorted(sm_dic,reverse=True)
        mx=max(sorted_values)
        del sorted_values[0]
        ans=-1
        mod=10**9+7
        for nm in sorted_values:
            prd=(nm*max(1,(mx-nm)))
            if prd>ans:
                ans=prd
        
        return ans%mod



