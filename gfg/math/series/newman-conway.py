"""
Newman Conway numbers is defined by the recurrence relation

P(n)=P(P(n-1))+P(n-P(n-1))

"""
import array

def seq(n):
    f=array.array('i',[0,1,1])
    # To store values of sequence in array
    for i in range(3,n+1):
        r=f[f[i-1]]+f[i-f[i-1]]
        f.append(r)
    
    return r



def sequence(n):
    if n==1 or n==2:
        return 1 
    else:
        return sequence(sequence(n-1)+sequence(n-sequence(n-1)))

