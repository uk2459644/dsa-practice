"""
Given an array arr[] of length N and an integer X, the task is to 
find the number of subsets with a sum equal to X.

"""
def subset_sum(a:list,n:int,sum:int):
    # initialize the matrix 
    tab=[[0]*(sum+1) for i in range(n+1)]
    tab[0][0]=1

    for i in range(1,sum+1):
        tab[0][i]=0
    
    for i in range(1,n+1):
        for j in range(sum+1):
            if a[i-1]<=j:
                tab[i][j]=tab[i-1][j]+tab[i-1][j-a[i-1]]
            else:
                tab[i][j]=tab[i-1][j]
    
    return tab[n][sum]



