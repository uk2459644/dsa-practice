from collections import defaultdict

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


descriptions = [[85,74,0],[38,82,0],[39,70,0],[82,85,0],[74,13,0],[13,39,0]]

# root=-1

graph=defaultdict(lambda: defaultdict(int))
children=set()
heads=set()
# children.add(-1)
for parent,child,isLeft in descriptions:
    children.add(child)
    heads.add(parent)
    graph[parent][isLeft]=child

def dfs(root):
    node=TreeNode(root)
    if graph[root][0]:
        node.right=dfs(graph[root][0])
    
    if graph[root][1]:
        node.left=dfs(graph[root][1])
    
    return node


root=heads.difference(children).pop()
# tree=dfs(root)

# print(tree)

print(graph,root)

