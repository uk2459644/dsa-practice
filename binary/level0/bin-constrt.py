# python program to construct binary tree
#  from given array in level order fashion tree node

# helper function that allocates a new node
class newNode:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=self.right=None

# function to insert nodes in level order
def insertLevelOrder(arr,i,n):
    root=None
    if i <n:
        root=newNode(arr[i])
        #  insert left child 
        root.left=insertLevelOrder(arr,2*i+1,n)
        # insert right child
        root.right=insertLevelOrder(arr,2*i+2,n)
    return root

# inorder fashion
def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

# driver code
if __name__=='__main__':
    

