# python code to check if a given number is 
# parse or not

def isSparce(n):
    if (n==1):
        return True
    global prev
    while (n>0):
        prev=n&1
        n=n>>1
        curr=n&1
        if (prev==curr and prev==1):
            return False
    return True

# time complexity O(log2n)
# auxiliary space O(1)

def checkSparse(n):
    if (n&(n>>1)):
        return 0
    return 1

# time complexity O(1)
# auxiliary space O(1)
