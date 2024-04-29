class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

class Solution:
    def cycleList(self,head:ListNode):
        if not head or not head.next:
            return None
        dc={}
        while head:
            if head in dc:
                return head
            dc[head]=1
            head=head.next
        return None



