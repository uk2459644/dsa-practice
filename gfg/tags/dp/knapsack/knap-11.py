"""
Partition problem using dynamic programming : 

The problem can be solved using dynamic programming when the sum of the 
elements is not too big. As the recomputations of the same subproblems can be
avoided by constructing a temporary array part[][] in a bottom-up manner
using the above recursive formula and it should satisfy the following formula:

part[i][j]=true if a subset of {arr[0],arr[1],...arr[j-1]} has sum equal to i,
otherwise false.

"""
"""
Follow the below steps to solve the problem: 

- First check if the sum of the element is even or not
- Declare a 2-D array part[][] of size (sum/2)+1*(N+1) 
- Run a for loop for 0<=i<=n and set part[0][i] equal to true as zero
  as any sum with zero elements is never possible

- Run a nested for loop for 1<=i<=sum/2 and 1<=j<=N 
  - Set part[i][j] equal to part[i][j-1]

"""

def findPartition(arr,n):
    sum=0
    i,j=0,0
    # calculate sum of all elements 
    for i in range(n):
        sum+=arr[i]
    
    if sum%2!=0:
        return False
    
    part=[[True for i in range(n+1)] for j in range(sum//2+1)]
    # Initializing top row as ture
    for i in range(0,n+1):
        part[0][i]=True
    # Initialize leftmost column as false
    for i in range(1,sum//2+1):
        part[i][0]=False
    
    # Fill the partition table in bottom up manner
    for i in range(1,sum//2+1):
        for j in range(1,n+1):
            part[i][j]=part[i][j-1]

            if i>= arr[j-1]:
                part[i][j]=(part[i][j] or part[i-arr[j-1]][j-1])

    return part[sum//2][n]


