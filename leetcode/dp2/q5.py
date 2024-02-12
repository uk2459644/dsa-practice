
string=input()
n=len(string)
# dp=[[False for i in range(n) ] for i in range(n)]

# every character itself is a palindrome
# for i in range(n):

#     dp[i][i]=True
ans=""
for start in range(n):
    for end in range(start,n):
        temp=string[start:end+1]
        if temp==temp[::-1] and len(temp)>len(ans):
            ans=temp
      
print(ans)




