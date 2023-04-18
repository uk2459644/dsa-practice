"""
Python code to count solution of 
a+b+c = n

"""
def countIntegralSolution(n):
    result=0
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i+j+k == n:
                    result+=1 
    
    return result

