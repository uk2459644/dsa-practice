class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def removeConsSum(self,head:ListNode):
        dummy=ListNode()
        dummy.next=head
        pref_sum=0
        dc={
            pref_sum:dummy
        }

        curr=dummy.next

        while curr:
            pref_sum+=curr.val
            if pref_sum in dc:
                temp=dc[pref_sum].next
                temp_sum=pref_sum+temp.val

                while temp !=curr:
                    del dc[temp_sum]
                    temp=temp.next
                    temp_sum+=temp.val
                
                dc[pref_sum].next=curr.next
            else:
                dc[pref_sum]=curr
            curr=curr.next
        
        return dummy.next


