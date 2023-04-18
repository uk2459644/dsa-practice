for _ in range(int(input())):
    x,y=map(int,input().split())
    z=x^y  
    a=2 
    ans=[2]
    if x%2==1:
        ans.append(x^a)
    
    if y%2==1:
        ans.append(y^a)
    
    if z%2==1:
        ans.append(z^a)
    
    ans.sort()
    print(*ans)