
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverseBetween(self,head:ListNode,left:int,right:int):
        dummy_node=ListNode()
        dummy_node.next=head
        pre=dummy_node

        for _ in range(left-1):
            pre=pre.next
        
        cur=pre.next
        for _ in range(right-left):
            next=cur.next
            cur.next=next.next
            next.next=pre.next
            pre.next=next
        
        return dummy_node.next
        



