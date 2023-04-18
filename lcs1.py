import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def lcs(X, Y):
    # Initializing X dp array of size
    n = len(X)
    m = len(Y)
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


for _ in range(inp()):
    n=inp()
    n_str=insr()
    mx=0
    for i in range(n):
        x_str=n_str[:i]
        y_str=n_str[i:]
        y_str=y_str[::-1]
        ans=lcs(x_str,y_str)
        mx=max(ans,mx)

    print(mx)