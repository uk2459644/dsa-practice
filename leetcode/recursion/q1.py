class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.left=left
        self.right=right

class Solution:
    def possibleTree(self,n:int):
        dp={0:[],1:[TreeNode()]}

        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res=[]
            for l in range(n):
                r=n-1-l
                leftTree,rightTree=backtrack(l),backtrack(r)

                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0,t1,t2))
            
            dp[n]=res

            return res
        
        return backtrack(n)




