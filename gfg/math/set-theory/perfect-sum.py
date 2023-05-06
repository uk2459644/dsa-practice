"""
Given an array of integers and a sum, the task is to print all subsets of the
given array with a sum equal to a given sum.

"""
# dp[i][j] is going to store True if sum j is possible with array
# elements from 0 to i.
dp=[[]]

def display(v):
    print(v)

# A recursive function to print all subsets with the help of dp[][].
# list p[] stores current subset.

def printSubsetsRec(arr,i,sum,p):
    # if we reached end and sum is non-zero. We print p[] only if 
    # arr[0] is equal to sum Or dp[0][sum] is True

    if (i==0 and sum !=0 and dp[0][sum]):
        p.append(arr[i])
        display(p)
        p=[]
        return
    
    

