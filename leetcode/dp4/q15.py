class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_sum(root):
    if not root:
        return []
    result = []
    current_level = [root]
    while current_level:
        level_sum = sum(node.value for node in current_level)
        result.append(level_sum)
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current_level = next_level
    return result

def dfs(root,arr:list):
    if root:
        dfs(root.left,arr)
        arr.append(root.value)
        dfs(root.right,arr)

# Example usage:
# Construct a sample binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

result = level_sum(root)
ans=[]
dfs(root,ans)
print(result,ans)
