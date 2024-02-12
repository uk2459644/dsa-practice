"""
Given an array arr[] consisting of N binary strings, and two integers A
and B, the task is to find the length of the longest subset consisting of
at most A 0s and B 1s.

Naive Approach: the simplest approach to solve the above problem is to use
recursion. At every recursive call, the idea is to either include or exclude the
current string. Once, all possiblities are considered, print the maximum length
of subset obtained.

"""
# function to count 0's in a string

def count0(s):
    # stores count of 0s
    count=0
    # iterate over characters of string
    for i in range(len(s)):
        # if current character is '0'
        if s[i]=='0':
            count+=1 
    
    return count

# Recursion function to find the length of longest subset from an array
# of strings with at most A 0's and B 1's

def solve(vec,A,B,idx):
    # if idx is equal to N 
    # or A+B is equal to 0
    if (idx==len(vec) or A+B==0):
        return 0
    
    # stores the count of 0's in arr[idx]
    zero=count0(vec[idx])
    # stores the count of 1's in arr[idx]
    one=len(vec[idx])-zero
    # stores the length of the subset if arr[i] is included
    inc=0
    # If zero is less than or equal to A and one is less than or equal to B
    if (zero<=A and one<=B):
        inc=1+solve(vec,A-zero,B-one,idx+1)
    # stores the length of the subset if arr[i] is excluded
    exc=solve(vec,A,B,idx+1)

    # return max of inc and exc
    return max(inc,exc)


"""
Efficient Approach: The above approach can be optimized using Memoization, based
on the following observations: 

It can be  observed that there exists a overlapping subproblem and optimal
substructure property.
Therefore the idea is to use dynamic programming to optimize the above approach.

The idea is to use the 3D-state dynamic programming.

Suppose Dp(i,A,B) represents the maximum length of the subset with at most A 0s and
B 1s.

Then the transition of states can be defined by either selecting a string at ith index or not,
- Dp(i,A,B)=MAx(1+Dp(i+1,A-z,B-o),Dp(i+1,A,B))

"""

# Function to count number of 0s present in the string
def count0(s):
    # store the count of 0s
    count=0
    # Iterate over characters of string
    for i in range(len(s)):
        # if current character is '0'
        if (s[i]=='0'):
            count+=1 
    
    return count

# Recursive function to find the length of longest subset from given
# array of strings with at most A 0s and B 1s

def solve(vec,A,B,idx,dp):
    # if idx is equal to N or A+B is equal to 0
    if (idx==len(vec)) or (A+B)==0:
        return 0
    # if the state is already calculated 
    if (dp[A][B][idx]>0):
        return dp[A][B][idx]
    # stores the count of 0's
    zero=count0(vec[idx])
    # stores the count of 1's 
    one=len(vec[idx])-zero

    # stores the length of longest by including arr[idx]
    inc=0
    # if zero is less than A and one is less than B
    if (zero<=A and one<=B):
        inc=1+solve(vec,A-zero,B-one,idx+1,dp)
    
    # stores the length of longest subset by excluding arr[idx]
    exc=solve(vec,A,B,idx+1,dp)

    # Assign 
    dp[A][B][idx]=max(inc,exc)

    return dp[A][B][idx]



