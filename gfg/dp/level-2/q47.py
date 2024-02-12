# Longest palindromic substring

# Given a string str, the task is to find the longest substring which is
#  a palindrome

"""
Follow the steps mentioned below to implement the idea: 

- Generate all the substring.
 - For each substring, check if it is palindrome or not.
 - If substring is palindrome, then update the result on the basis
   of longest palindromic substring
   found till now

"""
# A python solution for longest palindrome

# A function to print a substring str[low...high]

def printSubStr(str,low,high):
    for i in range(low,high+1):
        print(str[i],end="")

# This function prints the longest palindrome subString
# it also returns the length of the longest palindrome

def longestPalSubstr(str):
    # get length of input string
    n=len(str)
    # All subStrings of length 1 are palindromes
    maxLength=1
    start=0
    
    # Nested loop to mark start and end index
    for i in range(n):
        for j in range(i,n):
            flag=1
            # check palindrome
            for k in range(0,((j-i)//2)+1):
                if (str[i+k]!=str[j-k]):
                    flag=0
            
            # Palindrome
            if (flag !=0 and (j-i+1)>maxLength):
                start=i
                maxLength=j-i+1

                



