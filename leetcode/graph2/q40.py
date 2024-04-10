
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


root = [5,3,6,2,4,None,8,1,None,None,None,7,9]

n=len(root)

def buildTree(i):
    if i<n and root[i]!=None:
        node=TreeNode(root[i])
        node.left=TreeNode(2*i+1)
        node.right=TreeNode(2*i+2)

        return node
    return None

tree=buildTree(0)

result=[]
def dfs(node):
    if node:
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

dfs(tree)

print(result)





