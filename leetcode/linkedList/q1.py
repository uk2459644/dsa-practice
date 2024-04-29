class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def pairSum(self,head:ListNode):
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev,nxt=None,None

        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
            
        ans=0
        while prev:
            ans=max(ans,head.val+prev.val)
            prev=prev.next
            head=head.next
        
        return ans



