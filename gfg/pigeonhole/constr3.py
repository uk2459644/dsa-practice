"""
Given three binary strings a,b, and c each having 2*N characters each,
the task is to find a string having almost 3*N characters such that
at least two of the given three strings occur as its one of the subsequence.

"""
"""
Approach: 

- It can be observed that according to the Pigeonhole principle, there
  must exist a set of two strings such that the most frequent character
  in both the strings is the same and its frequency is >= N.

- Hence, for two such strings, a string of N most frequent characters
  can be created. The other remaining N characters of both the strings
  can be appended into the string respectively according to the order they
  occur. Therefore, the maximum size of the resultant string will be at
  most 3*N
  
"""
# Function to find most frequent character in the given string

def MostFrequent(s):
    # stores the frequency of 0 and 1 respectively
    arr=[0,0]

    for ch in s:
        arr[(ord(ch))-ord('0')]+=1 
    
    result = '0' if arr[0] > arr[1] else '1'

    return result

"""
Function to find a Binary string of at most 3N characters having at least
two of the given three strings of 2N characters as one of its subsequence
"""

def findStr(a,b,c):
    # stores most frequent char 
    freq = ""
    # Stores the respective string with most frequent values 
    s1,s2 = "",""
    # code to find the set of two strings with same most frequent 
    # characters 
    if (MostFrequent(a)==MostFrequent(b)):
        s1=a 
        s2=b 
        freq=MostFrequent(a)
    elif(MostFrequent(a)==MostFrequent(c)):
        s1=a
        s2=c 
        freq=MostFrequent(a)
    else:
        s1=b
        s2=c 
        freq = MostFrequent(b)
    # pointer to iterate strings 
    i,j=0,0 
    # Traversal using the two pointer approach 
    while (i<len(s1) and j<len(s2)):
        # if current character is not most frequent 
        while (i<len(s1) and s1[i]!=freq):
            print(s1[i],end="")
            i+=1 
        
        # if current character is not most frequent 
        while (j<len(s2) and s2[j]!=freq):
            print(s2[j],end="")
            j+=1 
        # if end of string is reached 
        if (i==len(s1) or j==len(s2)):
            break 
        
        # if both string character are same as most frequent 
        if (s1[i]==s2[j]):
            print(s1[i],end="")
            i+=1 
            j+=1 
        else:
            print(s1[i],end="")
            i+=1 
            

