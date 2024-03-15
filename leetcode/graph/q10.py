
class Solution:
    def replaceValueInTree(self,root):
        level_sum=[]

        def dfs(node,depth):
            if node:
                if len(level_sum)==depth:
                    level_sum.append(0)
                level_sum[depth]+=node.val
                dfs(node.left,depth+1)
                dfs(node.right,depth+1)
        
        def dfs2(node,depth):
            if node:
                node.val = level_sum[depth] - node.val

                if node.left and node.right:
                    siblings_sum=node.left.val+node.right.val
                    node.left.val=node.right.val=siblings_sum
                
                dfs2(node.left,depth+1)
                dfs2(node.right,depth+1)
        
        dfs(root,0)
        dfs2(root,0)

        return root



