class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:

    def allPossibleFBT(self,n:int):
        if n%2 == 0:
            return []
        
        memo={}

        def dfs(n):
            if n in memo:
                return memo[n]
            
            




