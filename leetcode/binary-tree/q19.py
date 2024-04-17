
from collections import deque,defaultdict

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def mostFrequentSum(self,root:TreeNode):
        sm=defaultdict(int)

        def dfs(node):
            if node:
                left=dfs(node.left)
                right=dfs(node.right)

                val = node.val + left +right
                sm[val]+=1

                return val

            return 0

        dfs(root)

        mx=max(sm.values())
        ans=[]

        for k,v in sm.items():
            if v== mx:
                ans.append(k)

        return ans     





