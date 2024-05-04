class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def deleteDuplicate(self,head:ListNode):
        dummy=ListNode(-1000)
        dummy.next=head
        prev=dummy
        curr=dummy.next

        while curr and curr.next:
            if curr.val == curr.next.val:
                end=curr

                while end and end.val == curr.val:
                    end=end.next
                
                prev.next=end
                curr=end
            else:
                prev=curr
                curr=curr.next
        
        return dummy.next


