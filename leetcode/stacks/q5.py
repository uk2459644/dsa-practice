
class Solution:
    def validStack(self,pushed:list[int],popped:list[int]):
        i=0
        ans=True

        while len(pushed) or len(popped)>0:
            if i<0:
                i=0
            if pushed[i]==popped[0]:
                pushed.pop(i)
                i-=1
                popped.pop(0)
            elif pushed[i]!=popped[0] and i==len(pushed)-1:
                ans=False
                break
            else:
                i+=1
        
        return True


