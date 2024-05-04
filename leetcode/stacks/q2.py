
class Solution:
    def removeOuterParentheses(self,s:str):
        count=0
        ans=""

        for ch in s:
            if ch=="(":
                count+=1
                if count==1:
                    continue
                ans+="("
            elif ch==")":
                count-=1
                if count==0:
                    continue
                ans+=")"

        return ans


