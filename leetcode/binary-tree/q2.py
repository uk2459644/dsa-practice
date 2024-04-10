class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def constructMaximum(self,nums:list):

        def dfs(lst:list):
            if not lst:
                return None
            mx,ind=-1,-1
            for i in range(len(lst)):
                if lst[i]>mx:
                    mx=lst[i]
                    ind=i
            
            node=TreeNode(mx)
            first=lst[ind+1:]
            second=lst[:ind]
            node.right=dfs(first)
            node.left=dfs(second)

            return node
        
        return dfs(nums)
        



