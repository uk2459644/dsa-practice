class TreeNode:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None

def dfs(node:TreeNode,level:int,paths:list,x:int,y:int,parent:int):
    if not node:
        return
    if node.value==x:
        paths.append(level)
        paths.append(parent)
    if node.value==y:
        paths.append(level)
        paths.append(parent)
        # return
    dfs(node.left,level+1,paths,x,y,node.value)
    dfs(node.right,level+1,paths,x,y,node.value)
    level-=1

    
    

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
root.right.right=TreeNode(5)
x,y=4,5
paths=[]
dfs(root,0,paths,x,y,-1)

print(paths)

