# pythonn code to implement the approach

def optimalStrategyOfGame(arr,n):
    memo={}
    # recursive top down memoized solution
    def solve(i,j):
        if i>j or i>=n or j<0:
            return 0
        k=(i,j)

        if k in memo:
            return memo[k]
        
        # if the user choose ith coin, the oppenent can choose from
        # i+1th or jth coin. If he chooses i+1th coin, user is left with
        # [i+2,j] range. 
        option1=arr[i]+min(solve(i+2,j),solve(i+1,j-1))
        # if user choooses jth coin, opponent can choose ith coin or
        # j-1th coin.
        option2=arr[j]+min(solve(i+1,j-1),solve(i,j-2))

        # since the user wants to get maximum money
        memo[k]=max(option1,option2)

        return memo[k]
    
    return solve(0,n-1)


