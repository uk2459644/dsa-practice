"""
Edit distances

"""
# A Naive recursive program to find minimum number of operations to 
# convert str1 to str2

def editDistance(str1,str2,m,n):
    # if first string is empty, the only option is to
    # insert all characters of second string into first
    if m==0:
        return n
    
    # if second string is empty, the only option is to remove
    # all characters of first string
    if n==0:
        return m
    
    # If last characters of two strings are same, nothing much to do. 
    # Ignore last characters and get count for remaining strings
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    
    # If last characters are not same, consider all three operations on
    # last character of first string, recursively compute minimum cost for 
    # all three operations and take minimum of three values

    return 1+min(editDistance(str1,str2,m,n-1),editDistance(str1,str2,m-1,n),editDistance(str1,str2,m-1,n-1))

    


