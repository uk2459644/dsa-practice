from typing import List 
from queue import Queue

class Node:
    def __init__(self, val=0,left=None,right=None) -> None:
        self.val =val 
        self.left = left
        self.right = right 

# function to convert the array to BST 
# and return the root of the created tree

def sortedArrayToBST(nums:List[int])->Node:
    if not nums:
        return None 
    n= len(nums)
    mid = n//2 
    root = Node(nums[mid])
    q=Queue()
    q.put((root,(0,mid-1)))
    q.put((root,(mid+1,n-1)))

    while not q.empty():
        curr = q.get()
        # get the parent nodes and its indices 
        parent = curr[0]
        left = curr[1][0]
        right = curr[1][1]
        if left <= right and parent is not None:
            mid=(left+right)//2
            child = Node(nums[mid])

            if nums[mid]<parent.val:
                parent.left = child
            else:
                parent.right = child
            q.put((child, (left,mid-1)))
            q.put((child,(mid+1, right)))
        
        return root