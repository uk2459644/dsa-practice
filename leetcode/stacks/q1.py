
class Solution:
    def removeOuterParentheses(self,s:str):
        count=0
        stack=[]
        ans=""

        for ch in s:
            if ch=="(":
                count+=1
                stack.append("(")
            elif ch==")":
                count-=1
                stack.append(")")
            
            if count==0:
                stack.pop()
                stack.pop(0)

                while len(stack)>0:
                    ans+=stack.pop(0)
        
        return ans


