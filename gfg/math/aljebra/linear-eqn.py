"""
The idea is to substract first coefficient from
rhs and then recur for remaining value of rhs.

"""

def countSol(coeff, start, end, rhs):
    # base case 
    if (rhs == 0):
        return 1 
    
    result = 0
    # one by one subtract all smaller or equal
    # coefficients and recur 
    for i in range(start,end+1):
        if (coeff[i]<=rhs):
            result +=countSol(coeff,i,end,rhs - coeff[i])
    
    return result 


