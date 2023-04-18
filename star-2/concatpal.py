for _ in range(int(input())):
    n,m=map(int,input().split())
    freq={}
    for c in input():
        add=(n>=m)-(n<m)
        if c in freq:
            freq[c]+=add 
        else:
            freq[c]=add
    
    for c in input():
        add=(m>n)-(m<=n)
        if c in freq:
            freq[c]+=add 
        else:
            freq[c]=add 
    
    odd=0
    for y in freq.values():
        odd+=y%2 
    
print("YES" if odd <=1 and min(freq.values())>=0 else "NO")