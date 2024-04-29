class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def removeNodes(self,head:ListNode):
        stack=[]
        curr=head

        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr=curr.next
        
        ans=ListNode()
        ans1=ans

        for node in stack:
            ans1.next=node
            ans1=ans1.next
        
        return ans.next


