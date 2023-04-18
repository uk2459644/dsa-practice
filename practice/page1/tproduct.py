import math

class newNode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def inOrder(arr,i,n):
    root=None
    if i<n:
        root=newNode(arr[i])
        root.left=inOrder(arr,2*i+1,n)
        root.right=inOrder(arr,2*i+2,n)
    return root

def getMax(root,ans):
    if root.left!=None and root.right!=None:
        a=root.left.data
        b=root.right.data
        if a!=None and b!=None:
            if a>b:
                ans.append(a)
                getMax(root.left,ans)
            else:
                ans.append(b)
                getMax(root.right,ans)
        elif  root.left!=None:
            ans.append(root.left.data)
            getMax(root.left,ans)
        elif root.right!=None:
            ans.append(root.right.data)
            getMax(root.right,ans)
    return ans

rn=True
mod=(10**9)+7
while rn:
    h=int(input())
    if h==0:
        rn=False
        continue
    nli=list(map(int,input().split()))
    n=len(nli)
    if h==1:
        print(nli[0])
        continue
    root=inOrder(nli,0,n)
    ansli=list()
    ansli.append(nli[0])
    anss=getMax(root,ansli)
    res=1 
    for nm in anss:
        res=(res*nm)%mod
    print(res)
        
        
