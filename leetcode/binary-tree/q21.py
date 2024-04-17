
class Solution:
    def validPreorder(self,preorder:str):
        tree=preorder.split(",")
        count=1
        for node in tree:
            count-=1
            if count<0:
                return False
            if node!="#":
                count+=2
        
        return True



