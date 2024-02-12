from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

def bfs(root):
    queue=deque([root])
    i=0
    while queue:
        current_length = len(queue)
        val=[n.val for n in queue[::-1]]
        if i%2==1:
            for idx,n in enumerate(queue):
                n.val = val[idx]
        for _ in range(current_length):
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        i+=1
    return root




