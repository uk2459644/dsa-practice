class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def oddEvenList(self,head:ListNode):
        ans=ListNode(-1)
        ans2=ListNode(-1)
        first=ans
        second=ans2
        curr=head

        while curr:
            if n%2==0:
                if second:
                    second.next=ListNode(curr.val)
                else:
                    second=ListNode(curr.val)
                second=second.next
            else:
                if first:
                    first.next=ListNode(curr.val)
                else:
                    first=ListNode(curr.val)
                first=first.next
            
            curr=curr.next
            n+=1
        if first:
            first.next=ans2.next
        
        return ans.next



