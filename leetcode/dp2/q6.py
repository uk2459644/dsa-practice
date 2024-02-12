
string=input()
n=len(string)

# Form a bottom-up dp 2d array
# dp[i][j] will be true if the string from i to j is a palindrome

dp=[[False for i in range(n)] for j in range(n)]
ans=""

# every string with one character is a palindrome
for i in range(n):
    dp[i][i]=True
    ans=string[i]

maxLen=1

for start in range(n-1,-1,-1):
    for end in range(start+1,n):
        # palindrome condition
        if string[start]==string[end]:
            # if it's a two char string or if the remaining is a palindrome
            dp[start][end]=True
            if maxLen<end-start+1:
                maxLen=end-start+1
                ans=string[start:end+1]

return ans








