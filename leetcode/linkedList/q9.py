class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverse(self,start,end_joint):
        prev,curr=end_joint,start
        while curr:
            nxt=curr.next
            curr.next=prev
            prev,curr=curr,nxt
        
        return prev
    def reverseEvenList(self,head:ListNode):
        if not head or not head.next:
            return head
        start_joint=head
        group_size=1
        while start_joint and start_joint.next:
            group_size+=1
            start=end=start_joint.next
            group_num=1

            while end and end.next and group_num < group_size:
                end=end.next
                group_num+=1
            
            if group_num % 2 !=0:
                start_joint=end
                continue
            end_joint=end.next
            start_joint.next=self.reverse(start,end_joint)
            start_joint=start
        
        return head


        


