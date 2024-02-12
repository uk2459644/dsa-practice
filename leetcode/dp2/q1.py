
string=input()
n=len(string)
word1=string
word2=string[::-1]

def find_longest_string(str1,str2,str3):
    # Find the length of each string
    len1=len(str1)
    len2=len(str2)
    len3=len(str3)
    # compare the lengths and return the longest string
    if len1>=len2 and len1>=len3:
        return str1
    elif len2>=len1 and len2>=len3:
        return str2
    else:
        return str3

def solve(word1,word2,pos1,pos2,n,count):
    if pos1>n or pos2>n:
        return count
    
    if word1[pos1]==word2[pos2]:
        count=count+word1[pos1]
        return solve(word1,word2,pos1+1,pos2+1,n,count)
    
    string1=solve(word1,word2,pos1+1,pos2,n,"")
    string2=solve(word1,word2,pos1,pos2+1,n,"")
    return find_longest_string(count,string1,string2)

print(solve(word1,word2,0,0,n-1,""))


