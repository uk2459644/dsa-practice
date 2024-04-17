class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def widthTree(self,root:TreeNode):
        if not root:
            return 0
        
        queue=[(root,0)]
        ans=0

        while queue:
            level_size=len(queue)
            left=queue[0][1]
            right=queue[-1][1]
            ans=max(ans,right-left+1)

            for i in range(level_size):
                node,pos=queue.pop(0)

                if node.left:
                    queue.append((node.left,pos*2+1))
                
                if node.right:
                    queue.append((node.right,pos*2+2))
        
        return ans
