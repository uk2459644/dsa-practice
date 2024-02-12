s=input()
p=input()
m,n=len(s),len(p)

def helper(i,j):
    if j==n:
        return i==m
    
    matching= i<m and (p[j]=='.' or s[i]==p[j])
    if j==n-1 or p[j]!='*':
        return matching and helper(i+1,j+1)
    
    return helper(i,j+2) or (matching and helper(i+1,j))




