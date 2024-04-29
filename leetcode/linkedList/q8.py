
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumber(self,l1:ListNode,l2:ListNode):
        num1,num2=0,0
        while l1 or l2:
            if l1:
                num1=num1*10+l1.val
                l1=l1.next
            if l2:
                num2=num2*10+l2.val
                l2=l2.next
        
        nums=str(num1+num2)
        ans=ListNode(-1)
        curr=ans

        for nm in nums:
            curr.next=ListNode(int(nm))
            curr=curr.next
        
        return ans.next
        



