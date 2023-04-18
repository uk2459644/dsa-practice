
def countSol(coeff,n,rhs):
    dp = [0 for i in range(rhs+1)]
    dp[0]=1 

    for i in range(n):
        for j in range(coeff[i],rhs+1):
            dp[j]+=dp[j-coeff[i]]
    
    return dp[rhs]

