num = "1432219"
k = 3

lst=[int(c) for c in num]
stack=[]

for nm in lst:
    while k>0 and stack and stack[-1]>nm:
        stack.pop()
        k-=1
    stack.append(nm)

while k>0 and stack:
    stack.pop()

while stack and stack[0]==0:
    stack.pop(0)

ans=""
for nm in stack:
    ans+=str(nm)

if len(stack)>0:
    print(ans)

print("0")

