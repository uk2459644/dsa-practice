class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def swapNodes(self,head:ListNode,k:int):
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        
        n=len(arr)
        arr[k-1],arr[n-k]=arr[n-k],arr[k-1]
        ans1=ListNode()
        ans=ans1
        for nm in arr:
            ans.next=ListNode(nm)
            ans=ans.next
        
        return ans1.next
        

