"""
Given an array arr[] of N integer elements, the task is to find the sum
of the average of all subsets of this array.

Naive approach: A naive solution is to iterate through all possible subsets, 
get an average of all of them and them one by one, but this will take exponential
time and will be infeasible for bigger arrays.

"""
def nCr(n,k):
    C=[[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if (j==0 or j==i):
                C[i][j]=1
            # calculate value using previously stored values
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    
    return C[n][k]

def resultOfAllSubsets(arr,N):
    result=0.0

    sum=0

    for i in range(N):
        sum+=arr[i]
    
    for n in range(1,N+1):
        result+=(sum*(nCr(N-1,n-1)))/n
    
    return result

