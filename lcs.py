
# implementation of lcs problem

def lcs(x,y):
    # find the length of the strings
    m=len(x)
    n=len(y)
    # declaring the array for storing the dp values
    l=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    
    return l[m][n]

for _ in range(int(input())):
    n=int(input())
    n_str=input()
    # n1=n//2
    # x_str=n_str[:n1]
    # y_str=n_str[n1:]
    # y_str=y_str[::-1]
    # ans=lcs(x_str,y_str)
    # print(ans)
    for i in range(n+1):
        x=n_str[:i]
        y=n_str[i:]
        y=y[::-1]
        print(x,y)