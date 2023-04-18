# Program to find miaximum product 
# of a level in Binary Tree 

# Helper function that allocates a new node with the given data
# and None left and right pointers.

class newNode:
    # constructor to create a new node 
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

# return difference of sums of odd
# level and even level 
def evenOddLevelDifference(root):
    if (not root):
        return 0
    
    # create a queue for level order traversal 
    q = []
    q.append(root)
    level = 0
    evenSum = 0
    oddSum =0 
    # traverse until the queue is empty 
    while (len(q)):
        size = len(q)
        level+=1
        # traverse for complete level
        while(size>0):
            temp = q[0]
            q.pop(0)
            # Check if levvel no. is even or odd 
            # and accordingly update the 
            # evenSum or oddSum
            if (level%2==0):
                evenSum+=temp.data 
            else:
                oddSum+=temp.data 
            # check for the left child 
            if (temp.left):
                q.append(temp.left)
            # check for right child 
            if (temp.right):
                q.append(temp.right)

            size-=1
    return (oddSum-evenSum)

