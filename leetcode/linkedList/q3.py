
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def spiralMatrix(self,m:int,n:int,head:ListNode):
        left=0
        right=n-1
        top=0
        bottom=m-1
        ans=[[-1]*n for _ in range(m)]

        if not head:
            return ans
        
        while head:
            for i in range(left,right+1):
                if head:
                    ans[top][i]=head.val
                    head=head.next
                else:
                    break
            top+=1
            for i in range(top,bottom+1):
                if head:
                    ans[i][right]=head.val
                    head=head.next
                else:
                    break
            right-=1
            for i in range(right,left-1,-1):
                if head:
                    ans[bottom][i]=head.val
                    head=head.next
                else:
                    break
            bottom-=1
            for i in range(bottom,top-1,-1):
                if head:
                    ans[i][left]=head.val
                    head=head.next
                else:
                    break
            for i in range(bottom,top-1,-1):
                if head:
                    ans[i][left]=head.val
                    head=head.next
                else:
                    break
            left+=1
        
        return ans




