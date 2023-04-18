# Python program to find k-th largest
# node using by reverse Morris traversal

class newNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.right = self.left = None 

def KthLargestUsingMorrisTraversal(root, k):
    curr = root 
    Klargest = None 
    # count variable to keep count
    # of visited nodes 
    count =0 
    while (curr!=None):
        if curr.right == None:
            count+=1
            if (count == k):
                Klargest = curr 
            # otherwise move to the left child
            curr = curr.left 
        else:
            succ = curr.right 
            # find inorder successor of current node
            while (succ.left != None and succ.left != curr):
                succ = succ.left 
            if (succ.left == None):
                succ.left = curr
                curr = curr.right 
            else:
                succ.left = None
                count+=1 
                if (count == k):
                    Klargest = curr
                curr = curr.left 
        return Klargest
    