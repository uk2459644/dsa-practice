class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def numComponents(self,head:ListNode):
        count=0
        prev=-1
        nums=set(nums)

        while head:
            if prev in nums and head.val not in nums:
                count+=1
            
            if head.val in nums and not head.next:
                count+=1
            
            prev=head.val
            head=head.next
        
        return count

